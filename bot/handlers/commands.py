from bot.bot import bot
from bot.database.users_requests import user_exists
from bot.handlers.menus import show_time_zones, show_main_menu

@bot.message_handler(commands=['start'])
def start_bot(message):
    if user_exists(user_id=message.from_user.id):
        show_main_menu(message=message)
        return
    show_time_zones(message=message)