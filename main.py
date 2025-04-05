import bot.handlers.__init__ 
from bot.handlers.reminders_service import start_reminder_service, stop_reminder_service
from bot.bot import bot

if __name__ == "__main__":
    try:
        start_reminder_service()
        bot.polling()
    except KeyboardInterrupt:
        stop_reminder_service()