import bot.handlers.__init__ # Import all handlers to register them
from bot.handlers.reminders_service import start_reminder_service, stop_reminder_service
from bot.bot import bot # Import the bot instance


# Import handlers so they get registered



if __name__ == "__main__":
    try:
        start_reminder_service()
        bot.polling()
        print("🤖 Bot is running...")
    except KeyboardInterrupt:
        print("Shutting down...")
        stop_reminder_service()