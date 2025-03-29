from bot.bot import bot
from bot.database.users_requests import add_user, update_timezone
from bot.database.users_requests import user_exists
from bot.handlers.menus import show_main_menu
from bot.handlers.menus import show_time_zones
from bot.utils.timezones import TIMEZONES


@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    #callback for timezones
    if call.data in TIMEZONES:
        handle_time_zones(call)
    elif call.data == "Change timezone":
        show_time_zones(message=call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)


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