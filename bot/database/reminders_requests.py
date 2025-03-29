from bot.database.connection import get_db_connection

def create_reminder(*, user_id: int, description: str, remind_at: str, repeat: str = None) -> None:
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL query to insert a new reminder
        query = """
            INSERT INTO reminders (user_id, description, remind_at, repeat, created_at, updated_at, is_active)
            VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, TRUE);
        """
        # Execute the query with provided data
        cursor.execute(query, (user_id, description, remind_at, repeat))

        # Commit the changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()
        print("Reminder created successfully.")
    except Exception as e:
        print(f"Error creating reminder: {e}")


def delete_reminder(*, reminder_id: int) -> None:
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL query to delete the reminder
        query = "DELETE FROM reminders WHERE id = %s"

        # Execute the query
        cursor.execute(query, (reminder_id,))

        # Commit the changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Reminder with ID {reminder_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting reminder: {e}")


def get_info_about_all_reminders(*, user_id: int) -> list:
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL query to get all reminders for a user
        query = "SELECT id, description, remind_at, created_at, updated_at, is_active FROM reminders WHERE user_id = %s"

        # Execute the query
        cursor.execute(query, (user_id,))
        reminders = cursor.fetchall()

        # Close the connection
        cursor.close()
        conn.close()

        # Return the list of reminders
        return reminders
    except Exception as e:
        print(f"Error getting reminders for user {user_id}: {e}")
        return []