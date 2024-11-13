# the correct password for entery is
correct_password = "12345"

# do not stop the loop untill the user gives the correct password
while True:
    # display the enter your password prompt
    password = input("Enter your password: ")
   
    # analyse if the provided password is matching
    if password == correct_password:
        print("Access is granted.")
        break  # if the user enters correct password exit the loop
    else:
        print("the password is incorrect. access denied. Please try again.")