INVENTORY_FILE = "inventory.csv"

def load_inventory():
    # TODO: read the CSV file into the inventory.
    # Catch FileNotFoundError and start with an empty inventory on first run.
    global inventory
    global categories
    inventory = list()
    categories = set()
    temp = list()
    item = dict()
    try: 
        with open(INVENTORY_FILE, "r", encoding="utf-8") as f:
            f.readline()
            for x in f:
                temp = x.strip().split(",")
                item = {
                    "name" : temp[0],
                    "category" : temp[1],
                    "price" : temp[2],
                    "quantity" : temp[3]
                }
                inventory.append(item)
                categories.add(item["category"])
    except FileNotFoundError:
        print("File khong ton tai!")

def view_inventory():
    # TODO: print every product in the inventory.
    print("-" * 67)
    print(f"{'Name':<25} {'Category':<20} {'Price':<10} {'Quantity':<10}")
    print("-" * 67)
    for i in inventory:
        name = i["name"]
        category = i["category"]
        price = i["price"]
        quantity = i["quantity"]
        print(f"{name:<25} {category:<20} {price:<10} {quantity:<10}")

def check_duplicate(name):
    for i in inventory:
        if(i["name"].lower() == name.lower()):
            raise Exception

def add_product():
    # TODO: prompt for name/category/price/quantity, add it to the inventory,
    # and update the set of categories. Handle non-numeric price/quantity input.
    nItems = int(input("- Number of items: "))
    for i in range(nItems):
        while True:
            try:
                print(f"----- Item {i+1} -----")
                name = input("+ Name: ")
                check_duplicate(name)
                category = input("+ Category: ")
                price = input("+ Price: ")
                quantity = input("+ Quantity: ")
                item = dict(name = name, category = category, price = price, quantity = quantity)
                inventory.append(item)
                categories.add(category)
                break
            except Exception as e:
                print("Product existed ! Please check again")

load_inventory()
#add_product()
view_inventory()