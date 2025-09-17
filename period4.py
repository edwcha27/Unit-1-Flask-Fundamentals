itemName = input("enter the item name:")
quantity = int(input(f"How many {itemName}?"))
price = float(input("Enter the price"))

if quantity > 0 and price > 0:
    print(f"Total Price: {price} of {quantity} {itemName}s")
else:
    print("Error: Invalid Inputs!")