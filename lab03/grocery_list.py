# Create an empty grocery list
grocery_list = []

# Continue showing the menu until the user chooses to clear the list
while True:
    print("Welcome to Your Shopping List!")
    print()
    print("Please make a selection from one of the following options:")
    print("1. Add an item to the shopping list.")
    print("2. Display the shopping list.")
    print("3. Display the item count.")
    print("4. Display the first item in the shopping list.")
    print("5. Display the last item in the shopping list.")
    print("6. Clear the shopping list.")

    selection = input("Selection: ")

    # Add an item to the grocery list
    if selection == "1":
        item = input("Item to add: ")
        grocery_list.append(item)

    # Display the grocery list
    elif selection == "2":
        print(grocery_list)

    # Display the number of items
    elif selection == "3":
        print(f"ITEM COUNT: {len(grocery_list)}")

    # Display the first item
    elif selection == "4":
        print(f"FIRST ITEM: {grocery_list[0]}")

    # Display the last item
    elif selection == "5":
        print(f"LAST ITEM: {grocery_list[-1]}")

    # Clear the grocery list
    elif selection == "6":
        grocery_list = []
        break

    # Display an error message for an invalid option
    else:
        print("You entered an invalid option. Goodbye!")
        break