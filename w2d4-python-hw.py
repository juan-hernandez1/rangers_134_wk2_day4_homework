# 2) Build a Shopping Cart
# You can use either lists or dictionaries. 
#The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

cart =  {}

while True:

    response = input("What would you like to do? add/delete/view/quit: ")

    if response == "add":
        new_item = input("What would you like to add? ")        
        quantity = int(input(f"How many {new_item} would you like to add? "))
        cart[new_item] = cart.get(new_item, 0) + quantity
        print(f"Qty {quantity}: {new_item}  has been added to your cart. ")
    elif response == "delete":
        takeout = input("What would you like to remove? ")
        quantity = int(input(f"How many {takeout} would you like to remove? "))
        if takeout in cart and cart[takeout] > 0:
            cart[takeout] -= quantity
            print(f"Qty {quantity}: {takeout} has been removed from your cart.")
        else:
            print(f"{takeout} is not in your cart.")
    elif response == "view":
            print("This is what is in your cart:")
            for item in cart.items():
                print(f"{item}")
    elif response == "quit":
        break
    else:
        print("Invalid input. Please choose add, delete, view, or quit.")
        
print("This is what is in your cart:")
for item in cart.items():
    print(f"{item}")