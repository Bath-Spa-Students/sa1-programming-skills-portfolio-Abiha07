# display the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# provide a name for search
search_name = input("provide a name to search for: ")

# Search for the name in the list
if search_name in names:
    print(f"{search_name} was successfuly founded in the list.")
else:
    print(f"{search_name} was not found in the list.")
