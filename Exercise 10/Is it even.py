# program to check if a number is even or odd
def check_even_odd(number):
    # If the number is  divisible by 2, it's even
    if number % 2 == 0:
        return f"{number} is even."
    else:
        # If not, it's odd
        return f"{number} is odd."

# Main function to handle user gethered info and display the result
def main():
    # let the user  enter a number
    try:
        user_number = int(input(" Enter a number: "))
        # Call the check_even_odd function and get the result message
        result_message = check_even_odd(user_number)
        # Print the result message
        print(result_message)
    except ValueError:
        # If the user enters a non-integer value, display an error message
        print("Invalid input. Please enter a numerical value.")

# Only run the main function if this script is run directly
if __name__ == "__main__":
    main() 
