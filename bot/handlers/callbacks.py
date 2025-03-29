from bot.bot import bot
from bot.database.users_requests import add_user, update_timezone, user_exists, get_user_timezone
from bot.database.reminders_requests import create_reminder, delete_reminder, get_info_about_all_reminders
from bot.handlers.menus import show_main_menu
from bot.handlers.menus import show_time_zones
from bot.utils.timezones import TIMEZONES, convert_to_utc


@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    #callback for timezones
    if call.data in TIMEZONES:
        handle_time_zones(call)
    elif call.data == "Change timezone":
        show_time_zones(message=call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    elif call.data == "Create reminder":
        handle_reminder_creation(call=call)


def handle_time_zones(call):
    tz = call.data  # This is the timezone selected by the user
    user_id = call.from_user.id
    #Update user's timezone if user already in db
    if user_exists(user_id=user_id):
        update_timezone(user_id=user_id, new_timezone=tz)
    else:
        add_user(user_id=user_id, timezone=tz)
    
    bot.send_message(chat_id=call.message.chat.id, text=f"You succesfully changed timezone, now your time zone is {tz}")
    bot.delete_message(call.message.chat.id, call.message.message_id)
    show_main_menu(message=call.message)


def handle_reminder_creation(call):
    user_id = call.from_user.id
    if not user_exists(user_id=user_id):
        bot.send_message(chat_id=call.message.chat.id, text="Please choose your timezone first")
        bot.delete_message(call.message.chat.id, call.message.message_id)
        show_main_menu(message=call.message)
        return
     
    msg = bot.send_message(chat_id=call.message.chat.id, text="Please enter reminder title: ")
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.register_next_step_handler(msg, process_reminder_time)


def process_reminder_time(message):
    chat_id = message.chat.id
    reminder_title = message.text

    msg = bot.send_message(chat_id=chat_id, text="Please send date and time for reminder in format Year:Month:Day Hour:Minute")

    bot.register_next_step_handler(msg, add_reminder_to_db, reminder_title)


def add_reminder_to_db(message, reminder_title):
    user_id = message.from_user.id
    reminder_time = message.text
    user_timezone = get_user_timezone(user_id=user_id)
    reminder_time_utc = convert_to_utc(remind_at=reminder_time, user_timezone=user_timezone)

    #Check if convertation was succed
    if reminder_time_utc:
        create_reminder(user_id=user_id, description=reminder_title, remind_at=reminder_time_utc)
        bot.send_message(chat_id=message.chat.id, text=f"Your reminder \"{reminder_title}\" was created succesfully!")
        show_main_menu(message=message)
    else:
        bot.send_message(chat_id=message.chat.id, text="Smth went wrong, may be your date format wasnt right, try again.")
        bot.register_next_step_handler(message, add_reminder_to_db, reminder_title)
    

