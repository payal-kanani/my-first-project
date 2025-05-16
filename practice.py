from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Print the current date, time, and year
print("Current Date and Time:", current_datetime)
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)
print("Microsecond:", current_datetime.microsecond)
print("Weekday:", current_datetime.weekday())  # Monday is 0 and Sunday is 6