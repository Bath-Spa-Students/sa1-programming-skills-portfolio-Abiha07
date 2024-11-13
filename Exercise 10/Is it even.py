# program to decide if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Main program
def main():
    # Ask the user to enter  a number
    try:
        user_number = int(input("Enter a number: "))
       
        # Call the program and get the result
        result = check_even_odd(user_number)
       
        # Print the result
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

# Run the main program
if __name__ == "__main__":
    main()