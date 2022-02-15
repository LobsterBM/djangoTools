import time
from datetime import datetime


def currentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time