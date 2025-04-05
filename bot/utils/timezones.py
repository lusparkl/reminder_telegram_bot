from datetime import datetime
import pytz

TIMEZONE_OFFSETS = {
    "UTC-12": -12, "UTC-11": -11, "UTC-10": -10, "UTC-9": -9, 
    "UTC-8": -8, "UTC-7": -7, "UTC-6": -6, "UTC-5": -5, 
    "UTC-4": -4, "UTC-3": -3, "UTC-2": -2, "UTC-1": -1, 
    "UTC": 0, "UTC+1": 1, "UTC+2": 2, "UTC+3": 3, 
    "UTC+4": 4, "UTC+5": 5, "UTC+6": 6, "UTC+7": 7, 
    "UTC+8": 8, "UTC+9": 9, "UTC+10": 10, "UTC+11": 11, "UTC+12": 12
}

TIMEZONES = [
    "UTC-12", "UTC-11", "UTC-10", "UTC-9", "UTC-8", "UTC-7", "UTC-6", "UTC-5", 
    "UTC-4", "UTC-3", "UTC-2", "UTC-1", "UTC+0", "UTC+1", "UTC+2", "UTC+3", 
    "UTC+4", "UTC+5", "UTC+6", "UTC+7", "UTC+8", "UTC+9", "UTC+10", "UTC+11", 
    "UTC+12"
]

def convert_to_utc(*, remind_at: str, user_timezone: str) -> str:
    try:
        time_format = "%Y-%m-%d %H:%M"

        if "UTC" in user_timezone:
            offset = int(user_timezone.replace("UTC", ""))
            pytz_timezone = f"Etc/GMT{-offset}"  # Reverse sign due to pytz convention
        else:
            pytz_timezone = user_timezone  # If user provides valid timezone (e.g., "Europe/Berlin")

        user_tz = pytz.timezone(pytz_timezone)

        local_time = datetime.strptime(remind_at, time_format)  # Parse time string
        local_time = user_tz.localize(local_time)  # Attach timezone info

        utc_time = local_time.astimezone(pytz.utc)

        return utc_time.strftime(time_format)
    
    except Exception as e:
        print(f"Error converting time to UTC: {e}")
        return None

def convert_from_utc(utc_time: datetime, user_timezone: str) -> str:
    try:
        time_format = "%Y-%m-%d %H:%M"

        if "UTC" in user_timezone:
            offset = int(user_timezone.replace("UTC", ""))
            pytz_timezone = f"Etc/GMT{-offset}"  # Reverse sign due to pytz convention
        else:
            pytz_timezone = user_timezone  # Use valid timezone name

        utc_zone = pytz.utc
        local_zone = pytz.timezone(pytz_timezone)

        utc_dt = utc_zone.localize(utc_time)

        local_dt = utc_dt.astimezone(local_zone)

        return local_dt.strftime(time_format)

    except Exception as e:
        print(f"Error converting time from UTC: {e}")
        return None