# List of names for the search
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# display prompt to the user to enter the name they are looking for
search_name = input(" Enter the name you want to search for: ").strip()

# Flag to track whether the name is found during the search
found = False

# Loop through each name in the list to check if it matches the user's input
for name in names:
    # Convert both names to lowercase to ensure the search is case-insensitive
    if name.lower() == search_name.lower():
        # If a match is found, set 'found' to True and inform the user
        found = True
        print(f"your search '{search_name}' is in the list.")
        break  # Exit the loop early since we found the name

# If the loop completes and the name wasn't found, let the user know
if not found:
    print(f"something went wrong, '{search_name}' is not in the list.")