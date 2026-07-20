from datetime import datetime as dt

actualDate = dt.now().date()
actualTime = dt.now().strftime("%X")
print(f"Today is {actualDate} and it is {actualTime}.")
