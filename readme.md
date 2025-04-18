## Documentation

### 1. Introduction
The Reminder Telegram Bot is a Python-based application that allows users to set reminders and receive notifications via Telegram. It is designed to handle multiple users, time zones, and scheduled tasks efficiently. This documentation provides an overview of the project's components, their functionality, and how they interact.

---

### 2. Components

#### 2.1 `main.py`
- **Purpose**: Entry point of the application.
- **Functionality**: Initializes the bot and starts the main event loop.

#### 2.2 `config.py`
- **Purpose**: Stores configuration settings and environment variables.
- **Functionality**: Reads sensitive data like API tokens and database credentials from a `.env` file.

#### 2.3 `bot/`
- **Purpose**: Contains the core logic for the Telegram bot.
- **Submodules**:
  - `bot.py`: Initializes the Telegram bot and sets up command handlers.
  - `handlers/`: Contains modules for handling user interactions.
    - `commands.py`: Handles bot commands like `/start` and `/help`.
    - `callbacks.py`: Processes callback queries from inline buttons.
    - `menus.py`: Renders interactive menus for users.
    - `reminders_service.py`: Manages background tasks for sending reminders.
  - `database/`: Manages database operations.
    - `connection.py`: Establishes a connection to the PostgreSQL database.
    - `reminders_requests.py`: Handles CRUD operations for reminders.
    - `users_requests.py`: Handles CRUD operations for user data.
  - `utils/`: Provides utility functions.
    - `timezones.py`: Handles time zone conversions and calculations.

---

### 3. Workflow

#### 3.1 User Registration
1. A new user interacts with the bot.
2. The bot registers the user in the database, storing their chat ID and time zone.

#### 3.2 Creating a Reminder
1. The user provides a title and a date/time for the reminder.
2. The bot converts the time to UTC and stores it in the database.

#### 3.3 Sending Notifications
1. The `reminders_service.py` module checks for due reminders every minute.
2. Notifications are sent to users via Telegram when reminders are due.

---

### 4. Database Schema

#### 4.1 Users Table
- **Columns**:
  - `id`: Primary key.
  - `chat_id`: Telegram chat ID.
  - `timezone`: User's time zone.

#### 4.2 Reminders Table
- **Columns**:
  - `id`: Primary key.
  - `user_id`: Foreign key referencing the `Users` table.
  - `title`: Title of the reminder.
  - `reminder_time`: Scheduled time for the reminder (in UTC).

---

### 5. API Integration

#### 5.1 Telegram Bot API
- **Purpose**: Facilitates communication between the bot and Telegram servers.
- **Usage**: The `telebot` library is used to send and receive messages, handle commands, and process user interactions.

---

### 6. Scheduling

#### 6.1 APScheduler
- **Purpose**: Manages background tasks for checking and sending reminders.
- **Usage**: A job is scheduled to run every minute to check for due reminders.

---

### 7. Error Handling
- **Database Errors**: Handled using try-except blocks in database modules.
- **API Errors**: Handled using error handlers provided by the `telebot` library.
- **User Input Validation**: Ensures that user-provided data (e.g., dates and times) is valid before processing.

---

### 8. Testing
- **Unit Tests**: Test individual modules like `timezones.py` and database operations.
- **Integration Tests**: Test the interaction between the bot and the database.
- **Manual Testing**: Verify the bot's functionality by interacting with it on Telegram.

---

### 9. Deployment
- **Steps**:
  1. Set up a PostgreSQL database.
  2. Deploy the bot on a server or cloud platform.
  3. Use a process manager like `systemd` or `supervisord` to keep the bot running.

---

### 10. Future Enhancements
- Add support for recurring reminders.
- Implement a web interface for managing reminders.
- Add localization for multiple languages.
- Enhance error handling and logging.