# start by creating a loop to collect pizza toppings
print("Enter 'quit' to stop adding toppings.")
while True:
    topping = input("which topping would you like on the pizza: ")
    
    if topping.lower() == 'quit':
        print("your order is finished!")
        break
    else:
        print(f"Adding {topping} to your pizza!") 
