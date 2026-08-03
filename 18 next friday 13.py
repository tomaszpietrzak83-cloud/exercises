from datetime import datetime
from datetime import timedelta


def friday_the_13th():
    currentDate = datetime.now()
    while True:
        presentDay = currentDate.day
        dayOfWeek = currentDate.weekday()
        if presentDay == 13 and dayOfWeek == 4:
            break
        else:
            currentDate = currentDate + timedelta(days=1)

    return currentDate.isoformat()
