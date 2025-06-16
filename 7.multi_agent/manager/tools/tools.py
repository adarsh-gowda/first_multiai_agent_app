from datetime import datetime


def get_current_time() -> dict:
    """
    Get the current time in the format MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%m-%d %H:%M:%S"),
    }