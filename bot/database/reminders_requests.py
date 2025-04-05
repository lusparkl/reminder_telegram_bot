from bot.database.connection import get_db_connection

def create_reminder(*, user_id: int, description: str, remind_at: str, repeat: str = None) -> None:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO reminders (user_id, description, remind_at, repeat, created_at, updated_at, is_active)
            VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, TRUE);
        """
        cursor.execute(query, (user_id, description, remind_at, repeat))

        conn.commit()
        cursor.close()
        conn.close()
        print("Reminder created successfully.")
    except Exception as e:
        print(f"Error creating reminder: {e}")


def delete_reminder(*, reminder_id: int) -> None:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM reminders WHERE id = %s"

        cursor.execute(query, (reminder_id,))

        conn.commit()
        cursor.close()
        conn.close()
        print(f"Reminder with ID {reminder_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting reminder: {e}")


def get_info_about_all_reminders(*, user_id: int) -> list:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT id, description, remind_at, created_at, updated_at, is_active FROM reminders WHERE user_id = %s"

        cursor.execute(query, (user_id,))
        reminders = cursor.fetchall()

        cursor.close()
        conn.close()

        return reminders
    except Exception as e:
        print(f"Error getting reminders for user {user_id}: {e}")
        return []


def get_pending_reminders(current_time):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT id, user_id, description, remind_at FROM reminders WHERE remind_at <= %s AND sent = FALSE"
    cursor.execute(query, (current_time,))
    reminders = cursor.fetchall()
    cursor.close()
    conn.close()
    return reminders

def mark_reminder_as_sent(reminder_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE reminders SET sent = TRUE WHERE id = %s"
    cursor.execute(query, (reminder_id,))
    conn.commit()
    cursor.close()
    conn.close()