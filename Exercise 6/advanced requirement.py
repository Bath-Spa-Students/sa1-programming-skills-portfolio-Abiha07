# Define the correct password for the system
correct_password = "codelab1"

# Set the maximum number of attempts which a user is allowed
max_attempts = 5

# lable a counter to track the number of attempts made by the user
attempts = 0

# Start a loop that will run until the correct password is entered or maximum attempts are reached
while attempts < max_attempts:
    # request the user to enter the password, with a message 
    user_password = input(" Enter the password: ").strip()
    
    # Increment the attempts counter by 1 after each entry
    attempts += 1

    # analyse if the entered password matches the correct password
    if user_password == correct_password:
        # If the password is correct, grant access and stop the loop
        print(" Welcome User!")
        break
    else:
        # Calculate remaining attempts to inform the user
        remaining_attempts = max_attempts - attempts
        # let the user know that the password is incorrect and display the remaining attempts
        print(f"Incorrect password. You have {remaining_attempts} attempt(s) remaining.")
        
        # If the user has reached the maximum allowed attempts, issue a final warning
        if attempts == max_attempts:
            print("Maximum attempts reached. Authorities have been alerted due to multiple failed access attempts.")
