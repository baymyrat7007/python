def cafe_order():
    print("Welcome to the Cafe!")
    menu = {
        "Coffe": {"type": "drinks", "price": 3}, 
        "Tea": {"type": "drinks", "price": 2}, 
        "Sandwich": {"type": "food", "price": 5}, 
        "Cake": {"type": "desserts", "price": 4},
    }
    order = {}

    while True:
        print("\nMenu: ")
        for item, details in menu.items():
            print(f"{item.capitalize()} ({details['type']}: {details['price']} $")
        item = input ("\nEnter the item you want to order or 'done':  ").strip().lower()     
        if item == "done":
            break
        if item not in menu:
            print("Invalid item. Please choose from the menu. ")
        quantity = input("Enter the quantity: ").strip()
        if quantity.isdigit():
            quantity = int(quantity)
            order[item] = order.get(item, 0 ) + quantity
            print(f"{quantity} {item} (s) added to your order.")
        else:
            print("Please enter a valid quantity. ")

    if order:
        print("\nYour order sum:  ")
        total = 0
        for item, qty in order.items():
            item_total = menu[item_total]["price"] * qty 
            print(f"{item.capitalize()} x {qty}: {item_total} $")
            total += item_total
        print(f"\nTotal amout: {total} $\nThank you for your order!")
    else:
        print("No items ordered. Thank you! ")
cafe_order()           