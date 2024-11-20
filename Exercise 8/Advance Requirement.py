# list of names to search from
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# display a Prompt to the user to enter a name they want to looking for
search_term = input("Enter the name you're looking for: ").strip()

# analyse if the entered name exists in the list, using a case-insensitive search
if search_term.lower() in [name.lower() for name in names]:
    # If the name is found, provide a friendly success message
    print(f"your search '{search_term}' is in the list.")
else:
    # If the name is not found, let the user know in a friendly way
    print(f"somthing went wrong, '{search_term}' isn't in the list.")
