#  the correct password for the system is
correct_password = "12345"

#  the maximum number of allowed password attempts
max_attempts = 3
 
# lable a counter to keep track of the number of attempts made
attempts = 0

# Start a loop that continues until the correct password is entered or attempts are completed
while attempts < max_attempts:
    # request the user to enter the password
    user_password = input("Please enter the password: ").strip()
    
    # Mask the entered password with asterisks for privacy
    masked_password = '*' * len(user_password)
    
    # Increase the attempt count by 1 after each entry
    attempts += 1

    # Check if the entered password matches the stored correct password
    if user_password == correct_password:
        # If correct, grant access and end the loop
        print(" Welcome User!")
        break
    else:
        # If incorrect, display an error message along with the masked password
        print(f"Incorrect password: {masked_password}")
        
        # Provide a hint if the user is on their second-to-last attempt
        if attempts == max_attempts - 1:
            print("Hint: The password is number.")
        
        # If the user has used all attempts, lock them out and tell them
        if attempts == max_attempts:
            print("Access denied. You have been locked out due to too many incorrect attempts.")
