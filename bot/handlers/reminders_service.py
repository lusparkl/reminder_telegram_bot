from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from bot.bot import bot
from bot.database.reminders_requests import get_pending_reminders, mark_reminder_as_sent
from bot.database.users_requests import get_user_timezone
from bot.utils.timezones import convert_from_utc
from bot.database.users_requests import get_chat_id

scheduler = BackgroundScheduler()

def process_due_reminders():
    now_utc = datetime.utcnow()  
    pending_reminders = get_pending_reminders(now_utc)

    for reminder in pending_reminders:
        user_id, description, = reminder[1], reminder[2]
        chat_id = get_chat_id(user_id=user_id)
        bot.send_message(chat_id, f"🔔 Reminder: *{description}*\n", parse_mode="Markdown")

        mark_reminder_as_sent(reminder[0])

def start_reminder_service():
    scheduler.add_job(process_due_reminders, 'interval', minutes=1)
    scheduler.start()
def stop_reminder_service():
    scheduler.shutdown()