# allow user to store information in the dictionary
name = input("write your name: ")
hometown = input("write your hometown: ")
age = input("write your age only in integers: ")
 
  # Store the gathered information in a dictionary
personal_info = {
  "Name": name,
  "Hometown": hometown,
  "Age": age,
}
  # Print the gathered information in separate lines
if age is not None:
  print(f"Name: {personal_info['Name']}")
  print(f"Hometown: {personal_info['Hometown']}")
  print(f"Age: {personal_info['Age']}")
else:
  print("Unable to display information due to invalid  input.")  