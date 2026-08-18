# NumPy practice — see NUMPY_EXERCISES.md for what each exercise asks.
# Write your code inside the matching function below.
# Work through them in order — later exercises reuse arrays built by
# earlier ones (stored as module-level variables: names, prices,
# quantities, prices_by_category).
#
# Runnable two ways:
#   - standalone: `python numpy_exercises.py` (shows its own submenu)
#   - from the CLI: `python main.py` -> option 7 "NumPy analysis"
#     (also opens this same submenu)
#
# Uses the real inventory data from inventory_operations.py / inventory.csv
# instead of hardcoded arrays, so this practice is tied to the actual CLI
# project.

import numpy as np
import inventory_operations as ops

names = None
prices = None
quantities = None
prices_by_category = None


def build_arrays_from_inventory():
    global names, prices, quantities

    ops.load_inventory()
    inventory = ops.inventory

    names = np.array([product["name"] for product in inventory])
    prices = np.array([product["price"] for product in inventory])
    quantities = np.array([product["quantity"] for product in inventory])


def slice_first_and_last_names():
    # TODO: use slicing to print the first 5 and the last 5 of `names`.
    pass


def find_low_stock_products():
    # TODO: boolean indexing — names of products with quantity < 10.
    pass


def compute_inventory_value():
    # TODO: prices * quantities per product, then the grand total value
    # of the whole shop with np.sum().
    pass


def find_most_expensive_product():
    # TODO: index and name of the most expensive product (np.argmax).
    pass


def reshape_prices_by_category():
    # TODO: reshape `prices` into a (5, 10) matrix (5 categories x 10
    # products each), store it in the module-level `prices_by_category`.
    pass


def sum_price_per_category():
    # TODO: total price sum per category — np.sum with the right axis
    # on prices_by_category.
    pass


def average_price_per_category():
    # TODO: average price per category — np.mean with axis.
    pass


def std_price_per_category():
    # TODO: std of price per category — np.std with axis.
    pass


def flatten_and_verify_prices():
    # TODO: flatten prices_by_category back to 1-D and confirm it's
    # identical to `prices` (np.array_equal).
    pass


def print_numpy_menu():
    print("\n----- NumPy Exercises -----")
    print("1. Slice first/last 5 product names")
    print("2. Boolean indexing: low-stock products (qty < 10)")
    print("3. Inventory value per product + grand total")
    print("4. Most expensive product (argmax)")
    print("5. Reshape prices into (5, 10) by category")
    print("6. Total price per category (axis sum)")
    print("7. Average price per category (axis mean)")
    print("8. Std of price per category (axis std)")
    print("9. Flatten back + verify equal to original")
    print("0. Back to main menu")


def run_numpy_analysis():
    # Mandatory first step — always run before showing the submenu, so
    # `names`/`prices`/`quantities` are never None when an exercise uses them.
    build_arrays_from_inventory()

    while True:
        print_numpy_menu()
        choice = input("Choose an exercise: ").strip()

        if choice == "1":
            slice_first_and_last_names()
        elif choice == "2":
            find_low_stock_products()
        elif choice == "3":
            compute_inventory_value()
        elif choice == "4":
            find_most_expensive_product()
        elif choice == "5":
            reshape_prices_by_category()
        elif choice == "6":
            sum_price_per_category()
        elif choice == "7":
            average_price_per_category()
        elif choice == "8":
            std_price_per_category()
        elif choice == "9":
            flatten_and_verify_prices()
        elif choice == "0":
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    run_numpy_analysis()
