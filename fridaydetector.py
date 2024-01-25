import datetime
from calendar import weekday

year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def is_friday_13th(year, month):
    """Checks if the 13th of a given month and year is a Friday."""

    day_13 = datetime.date(year, month, 13)
    weekday_number = day_13.weekday()  # 0 for Monday, 6 for Sunday
    return weekday_number == 4  # True if Friday, False otherwise

if is_friday_13th(year, month):
    print("Beware! It's Friday the 13th in", month, year)
    print("Here's a spooky image for you:")
    # Display a spooky image here (optional)
else:
    print("Phew! It's not Friday the 13th in", month_names[month], year)