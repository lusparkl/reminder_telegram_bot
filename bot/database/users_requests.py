from bot.database.connection import get_db_connection

def add_user(*, user_id: int, timezone: str) -> None:
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the user already exists
        cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
        existing_user = cursor.fetchone()

        if existing_user:
            print(f"User {user_id} already exists in the database.")
        else:
            # SQL query to insert a new user
            query = "INSERT INTO users (id, timezone) VALUES (%s, %s)"
            cursor.execute(query, (user_id, timezone))

            # Commit the changes and close the connection
            conn.commit()
            print(f"User {user_id} added to the database.")

        # Close the connection
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error adding user: {e}")

def user_exists(*, user_id: int) -> bool:
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the user exists in the database
        cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
        existing_user = cursor.fetchone()

        # Close the connection
        cursor.close()
        conn.close()

        # If user exists, return True
        return existing_user is not None
    except Exception as e:
        print(f"Error checking if user exists: {e}")
        return False
    
def update_timezone(*, user_id: int, new_timezone: str) -> None:
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQL query to update the timezone
        query = "UPDATE users SET timezone = %s WHERE id = %s"
        cursor.execute(query, (new_timezone, user_id))
        conn.commit()

        print(f"User {user_id}'s timezone updated to {new_timezone}.")

        # Close the connection
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error updating timezone: {e}")