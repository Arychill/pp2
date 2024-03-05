from datetime import datetime, timedelta

date = datetime.now()
delta = timedelta(days = 5)
print(f"Date right now: {(date).strftime('%c')}")
print(f"Subtract five days from current date: {(date - delta).strftime('%c')} \n")

delta2 = timedelta(days = 1)
print(f"Today: {date.strftime('%c')}")
print(f"Tomorrow: {(date + delta2).strftime('%c')}")
print(f"Yesterday: {(date - delta2).strftime('%c')}\n")

current_date = datetime.now()
date_without_microseconds = current_date.replace(microsecond=0)
print("Original Date:", current_date)
print("Date without Microseconds:", date_without_microseconds)


#Dates to write
date1 = datetime(2022, 1, 1, 12, 0, 0)
date2 = datetime(2022, 1, 2, 15, 30, 0)

time_difference = date2 - date1
difference_in_seconds = time_difference.total_seconds()

print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in seconds:", difference_in_seconds)