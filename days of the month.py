# create a dictionary that links each month number (1-12) to the number of days in that month for a non-leap year
days_in_month = {
    1: 31,   # January has 31 days
    2: 28,   # February has 28 days (in a non-leap year)
    3: 31,   # March has 31 days
    4: 30,   # April has 30 days
    5: 31,   # May has 31 days
    6: 30,   # June has 30 days
    7: 31,   # July has 31 days
    8: 31,   # August has 31 days
    9: 30,   # September has 30 days
    10: 31,  # October has 31 days
    11: 30,  # November has 30 days
    12: 31   # December has 31 days
}

# tell the user to enter a month number between 1 and 12
try:
    month_number = int(input(" Enter the month number (1-12): ").strip())  # Remove extra spaces around input

    # Analyse if the entered month number is within the valid range of 1 to 12
    if 1 <= month_number <= 12:
        
        # Special case for February (month 2), where we need to check for a leap year
        if month_number == 2:
            # Ask the user if the year is a leap year
            is_leap = input("Is it a leap year? (yes/no): ").strip().lower()
            # If it's a leap year, February will have 29 days; otherwise, it will have 28 days
            days = 29 if is_leap == "yes" else 28
        else:
            # For rest of the months, just look up the number of days in the dictionary
            days = days_in_month[month_number]
        
        # Output the number of days in the selected month
        print(f"The number of days in month {month_number} is {days}.")
    else:
        # Inform the user if the month number is invalid (not between 1 and 12)
        print(" That's not a valid month number. Please enter a number between 1 and 12.")

except ValueError:
    # check for  cases where the user inputs something that isn't a number 
    print(" that's not a valid input. Please enter a number between 1 and 12.")
