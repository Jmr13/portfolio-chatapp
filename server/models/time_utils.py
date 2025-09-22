import json
from datetime import datetime
from zoneinfo import ZoneInfo

TIMEZONE_DATA = {
    "tokyo": "Asia/Tokyo",
    "san francisco": "America/Los_Angeles",
    "paris": "Europe/Paris"
}

def get_current_time(location: str) -> str:
    """Get the current time for a given location."""
    location_lower = location.lower()
    
    timezone = next(
        (tz for city, tz in TIMEZONE_DATA.items() if city in location_lower), None
    )

    if timezone:
        current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
        return json.dumps({"current_time": current_time})
    else:
        return json.dumps({"current_time": "unknown"})