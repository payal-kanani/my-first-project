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

def get_person(month_string):
    '''
    This function takes a month (as a string parameter) and
    returns the name of the person whose birthday falls within that month
    '''
    lowercase_month = month_string.lower()
    birthday_person = birthdays_by_month.get(lowercase_month, 'Nobody')
    return birthday_person

month_name = input('What month is it?')

if month_name.lower() in birthdays_by_month.keys():
    print(f"This month it is {get_person(month_name)}'s birthday")
else:
    print('That\'s not a month!')