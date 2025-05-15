birthdays_by_month = {
    "january": "Alice",
    "february": "Bob",
    "march": "Charlie",
    "april": "Diana",
    "may": "Ethan",
    "june": "Fiona",
    "july": "George",
    "august": "Hannah",
    "september": "Ian",
    "october": "Julia",
    "november": "Kyle",
    "december": "Laura"
}

#month = "March"  # You can change this value to any month
#birth_name = birthdays_by_month.get(month.lower())


def get_person(month_string):
    """
    This function takes a month as input and returns the name of the person with a birthday in that month.
    """
    lowercase_month = month_string.lower()
    birthday_person =  birthdays_by_month.get(lowercase_month, "None")
    return birthday_person
    

month = input("Enter a month: ")
print(f"Happy birthday to {get_person(month)}")