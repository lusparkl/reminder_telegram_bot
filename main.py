import bot.handlers.callbacks
import bot.handlers.commands
import bot.handlers.menus
from bot.bot import bot # Import the bot instance


# Import handlers so they get registered


if __name__ == "__main__":
    print("🤖 Bot is running...")
    bot.infinity_polling()