# allow user to store information in the dictionary
name = "Abiha"  # Name as a string
hometown = "Pakistan"    # Hometown as a string
age = 19                 # Age as an integer

# Store the gathered information in a dictionary
info = {
    "Name": name,        # Key "Name" with the value of name
    "Hometown": hometown, # Key "Hometown" with the value of hometown
    "Age": age            # Key "Age" with the value of age
}

# Print the gathered information in separate line
print(f"{info['Name']}\n{info['Hometown']}\n{info['Age']}")