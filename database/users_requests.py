from database.connection import get_db_connection

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