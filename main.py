INVENTORY_FILE = "inventory.csv"


def load_inventory():
    # TODO: read the CSV file into the inventory.
    # Catch FileNotFoundError and start with an empty inventory on first run.
    pass


def save_inventory():
    # TODO: write the inventory back to the CSV file.
    pass


def find_product():
    # TODO: search the inventory by name, return (found: bool, index: int).
    pass


def add_product():
    # TODO: prompt for name/category/price/quantity, add it to the inventory,
    # and update the set of categories. Handle non-numeric price/quantity input.
    pass


def view_inventory():
    # TODO: print every product in the inventory.
    pass


def search_product():
    # TODO: prompt for a name, use find_product, print the result
    # or "Product not found".
    pass


def update_product():
    # TODO: prompt for a name, use find_product, update price/quantity
    # or print "Product not found".
    pass


def delete_product():
    # TODO: prompt for a name, use find_product, remove it
    # or print "Product not found".
    pass


def view_statistics():
    # TODO: print total products, total quantity, total value, categories.
    pass


def print_menu():
    print("\n===== INVENTORY MANAGEMENT =====")
    print("1. Add product")
    print("2. View all inventory")
    print("3. Search product by name")
    print("4. Update quantity/price")
    print("5. Delete product")
    print("6. View inventory statistics")
    print("0. Exit (auto-saves before exiting)")


def main():
    load_inventory()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            view_statistics()
        elif choice == "0":
            save_inventory()
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
