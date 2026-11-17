
def display_menu():
    print("\n--- Store Management System ---")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

def store_management():
    inventory = {}

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            if not inventory:
                print("\nInventory is empty.")
            else:
                print("\n--- Current Inventory ---")
                print(f"{'ID':<10} | {'Name':<15} | {'Quantity':<10} | {'Price ($)':<10}")
                print("-" * 52)
                for item_id, details in inventory.items():
                    print(f"{item_id:<10} | {details['name']:<15} | {details['qty']:<10} | {details['price']:<10.2f}")

        elif choice == '2':
            item_id = input("Enter Item ID: ").strip()
            if item_id in inventory:
                print("Error: Item ID already exists! Use update instead.")
                continue
            name = input("Enter Item Name: ").strip()
            try:
                qty = int(input("Enter Quantity: "))
                price = float(input("Enter Price: "))
                inventory[item_id] = {'name': name, 'qty': qty, 'price': price}
                print(f"Success: Item '{name}' added!")
            except ValueError:
                print("Error: Quantity must be an integer and price must be a number.")

        elif choice == '3':
            item_id = input("Enter Item ID to update: ").strip()
            if item_id not in inventory:
                print("Error: Item ID not found!")
                continue
            print(f"Updating item: {inventory[item_id]['name']}")
            try:
                qty = int(input("Enter new Quantity: "))
                price = float(input("Enter new Price: "))
                inventory[item_id]['qty'] = qty
                inventory[item_id]['price'] = price
                print("Success: Item updated!")
            except ValueError:
                print("Error: Quantity must be an integer and price must be a number.")

        elif choice == '4':
            item_id = input("Enter Item ID to delete: ").strip()
            if item_id in inventory:
                deleted_item = inventory.pop(item_id)
                print(f"Success: Item '{deleted_item['name']}' deleted!")
            else:
                print("Error: Item ID not found!")

        elif choice == '5':
            print("Exiting Store Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    store_management()