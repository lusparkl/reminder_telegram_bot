from database.connection import get_db_connection

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


def update_reminder_time(*, reminder_id: int, new_time: str) -> None:
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL query to update reminder time
        query = "UPDATE reminders SET remind_at = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s"

        # Execute the query with the new time
        cursor.execute(query, (new_time, reminder_id))

        # Commit the changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Reminder time for ID {reminder_id} updated to {new_time}.")
    except Exception as e:
        print(f"Error updating reminder time: {e}")


def get_info_about_reminder(*, reminder_id: int) -> tuple:
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL query to get reminder information
        query = "SELECT id, user_id, description, remind_at, created_at, updated_at, is_active FROM reminders WHERE id = %s"

        # Execute the query
        cursor.execute(query, (reminder_id,))
        reminder_info = cursor.fetchone()

        # Close the connection
        cursor.close()
        conn.close()

        # Return the reminder information
        return reminder_info
    except Exception as e:
        print(f"Error getting reminder info: {e}")
        return None


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