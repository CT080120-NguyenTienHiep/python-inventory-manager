from inventory_operations import (
    load_inventory,
    save_inventory,
    add_product,
    view_inventory,
    search_product,
    update_product,
    delete_product,
    view_statistics,
)
from numpy_exercises import run_numpy_analysis


def print_menu():
    print("\n===== INVENTORY MANAGEMENT =====")
    print("1. Add product")
    print("2. View all inventory")
    print("3. Search product by name")
    print("4. Update quantity/price")
    print("5. Delete product")
    print("6. View inventory statistics")
    print("7. NumPy analysis")
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
        elif choice == "7":
            run_numpy_analysis()
        elif choice == "0":
            save_inventory()
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")
