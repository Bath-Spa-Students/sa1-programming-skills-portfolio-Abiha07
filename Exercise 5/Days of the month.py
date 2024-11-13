# store the numbers of the months and the days in each month in a dictionary
month_days = {
    1: 31,
    2: 28,  
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# analytics to check for leap year
def is_this_leap_year(year):
    # Leap year if divisible by 4 and not 100, or divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# display to ask user to enter a month number to check
try:
    month = int(input("provide the month number (1-12): "))

    # Check if the month is valid
    if month in month_days:
        # check February for leap year
        if month == 2:
            year = int(input("please provide the year: "))
            if is_this_leap_year(year):
                print("February has 29 days becouse of leap year.")
            else:
                print("February has 28 days.")
        else:
            # display the number of days in the matching correct month
            print(f"The month {month} has {month_days[month]} days.")
    else:
        print("Invalid month number. Please provide a number between 1 and 12.")
except ValueError:
    print("Invalid input. Please provide a numeric value for the month.")