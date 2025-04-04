from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from bot.bot import bot
from bot.database.reminders_requests import get_pending_reminders, mark_reminder_as_sent
from bot.database.users_requests import get_user_timezone
from bot.utils.timezones import convert_from_utc
from bot.database.users_requests import get_chat_id

scheduler = BackgroundScheduler()

def process_due_reminders():
    """Fetch and send due reminders."""
    now_utc = datetime.utcnow()  # Current time in UTC
    pending_reminders = get_pending_reminders(now_utc)

    for reminder in pending_reminders:
        user_id, description, remind_at = reminder[1], reminder[2], reminder[3] 
        chat_id = get_chat_id(user_id=user_id)
        print(chat_id)
        # Convert reminder time to user's timezone
        # Send the reminder message
        bot.send_message(chat_id, f"🔔 Reminder: *{description}*\n", parse_mode="Markdown")

        # Mark the reminder as sent
        mark_reminder_as_sent(reminder[0])  # Assuming reminder[0] is the ID

def start_reminder_service():
    """Start the reminder service."""
    scheduler.add_job(process_due_reminders, 'interval', minutes=1)
    scheduler.start()

def stop_reminder_service():
    """Stop the reminder service."""
    scheduler.shutdown()