from bot.bot import bot
from telebot import types
from telebot.util import quick_markup
from bot.utils.timezones import TIMEZONES

def show_main_menu(*, message):
    markup = quick_markup({
    "Create reminder": {"callback_data": "Create reminder"},
    "All reminders": {"callback_data": "All reminders"},
    "Change timezone": {"callback_data": "Change timezone"},
}, row_width=2)
    bot.send_photo(chat_id=message.chat.id, photo="https://i.pinimg.com/originals/1f/a9/e5/1fa9e5cf373c22aba39df7f5754bca07.jpg", caption="Hello there👋! Choose what you wanna do:", reply_markup=markup)

def show_time_zones(*, message):
    markup = types.InlineKeyboardMarkup()
    for i in range(0, len(TIMEZONES), 2):
        buttons = TIMEZONES[i:i+2]
        markup.add(*[types.InlineKeyboardButton(text=tz, callback_data=tz) for tz in buttons])
    
    bot.send_photo(chat_id=message.chat.id, photo="https://images.pexels.com/photos/1616516/pexels-photo-1616516.jpeg?cs=srgb&dl=pexels-lastly-1616516.jpg&fm=jpg", caption="Please choose your timezone from provided below:", reply_markup=markup)

back_to_main_menu_markup = quick_markup({"Back to main menu": {"callback_data": "Back to main menu"}}, row_width=1)