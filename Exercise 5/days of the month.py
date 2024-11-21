# create a dictionary to store the number of days in each month
# Keys represent the month numbers and values represent the days in each month
days_in_month = {
    1: 31,   # January
    2: 28,   # February (assuming it as a non-leap year)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# Ask the user to input a month number
try:
    month_number = int(input(" Enter a month number (1-12): ").strip()) # .strip() Removes extra spaces around input

    # Check if the month number is within the valid range
    if month_number in days_in_month:
        # show the number of days for the entered month
        print(f"The number of days in month {month_number} is {days_in_month[month_number]}.")
    else:
        # Inform the user if the input is outside the range of 1-12
        print(" That's not a valid month number. Please enter a number between 1 and 12.")

except ValueError:
    # Handle non-integer input 
    print("Invalid input. Please enter a numerical value between 1 and 12.")
