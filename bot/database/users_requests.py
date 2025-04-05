from bot.database.connection import get_db_connection

def add_user(*, user_id: int, timezone: str, chat_id: int) -> None:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
        existing_user = cursor.fetchone()

        if existing_user:
            print(f"User {user_id} already exists in the database.")
        else:
            query = "INSERT INTO users (id, timezone, chat_id) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, timezone, chat_id))

            conn.commit()
            print(f"User {user_id} added to the database.")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error adding user: {e}")

def user_exists(*, user_id: int) -> bool:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM users WHERE id = %s", (user_id,))
        existing_user = cursor.fetchone()

        cursor.close()
        conn.close()

        return existing_user is not None
    except Exception as e:
        print(f"Error checking if user exists: {e}")
        return False
    
def update_timezone(*, user_id: int, new_timezone: str) -> None:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "UPDATE users SET timezone = %s WHERE id = %s"
        cursor.execute(query, (new_timezone, user_id))
        conn.commit()

        print(f"User {user_id}'s timezone updated to {new_timezone}.")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error updating timezone: {e}")

def get_user_timezone(user_id: int) -> str:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT timezone FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return result[0] if result else None
    
    except Exception as e:
        print(f"Error fetching timezone for user {user_id}: {e}")
        return None

def get_chat_id(user_id: int) -> int | None:
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT chat_id FROM users WHERE id = %s;", (user_id,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result[0]:
            return result[0]  # Return chat_id
        else:
            print(f"❌ No chat_id found for user {user_id}")
            return None

    except Exception as e:
        print(f"❌ Error fetching chat_id: {e}")
        return None
