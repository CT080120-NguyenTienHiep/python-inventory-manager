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
                    "price" : int(temp[2]),
                    "quantity" : int(temp[3])
                }
                inventory.append(item)
                categories.add(item["category"])
    except FileNotFoundError:
        print("File khong ton tai!")


def save_inventory():
    # TODO: write the inventory back to the CSV file.
    line = ""
    try:
        with open(INVENTORY_FILE,"w", encoding="utf-8") as f:
            f.writelines("name,category,price,quantity\n")
            for i in inventory:
                line = f"{i['name']},{i['category']},{i['price']},{i['quantity']}\n"
                f.writelines(line)
    except FileNotFoundError:
        print("File not exist!")

def find_product():
    # TODO: search the inventory by name, return (found: bool, index: int).
    productName = input("- Product name: ").lower()
    index = 1
    for i in inventory:
        if i["name"].lower() == productName :
            return tuple(("Found",index))
        index += 1
    return tuple(("Not found!",))

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
                price = int(input("+ Price: "))
                quantity = int(input("+ Quantity: "))
                item = dict(name = name, category = category, price = price, quantity = quantity)
                inventory.append(item)
                categories.add(category)
                print("Add product successful!")
                break
            except Exception as e:
                print("Product existed ! Please check again")


def view_inventory():
    # TODO: print every product in the inventory.
    place = 1
    print("-" * 70)
    print(f"{'Name':<30} {'Category':<18} {'Price':<10} {'Quantity':<10}")
    print("-" * 70)
    for i in inventory:
        name = i["name"]
        category = i["category"]
        price = i["price"]
        quantity = i["quantity"]
        print(f"{place:<2}. {name:<25} {category:<20} {price:<10} {quantity:<10}")
        place += 1


def search_product():
    # TODO: prompt for a name, use find_product, print the result
    # or "Product not found".
    searchRes = find_product()
    if searchRes[0] == "Found":
        print(f"--> Product located at: {searchRes[1]}")
    else:
        print("--> Product not found!")


def update_product():
    # TODO: prompt for a name, use find_product, update price/quantity
    # or print "Product not found".
    searchRes = find_product()
    if searchRes[0] == "Found":
        while True:
            try:
                price = int(input("- Enter new price: "))
                quantity = int(input("- Enter new quantity: "))
                if(price < 0 or quantity < 0):
                    raise ValueError
                else:
                    product = inventory[searchRes[1]-1]
                    product["price"] = price
                    product["quantity"] = quantity
                    print("--> Updated successful")
                    break
            except ValueError:
                print("* Value cannot be negative !")
    else:
        print("--> Product not found!")


def delete_product():
    # TODO: prompt for a name, use find_product, remove it
    # or print "Product not found".
    searchRes = find_product()
    if searchRes[0] == "Found":
        print("--> Are you sure to delete ?")
        choice = input(f"{'1.Yes':<10} {'2.No':<10} -->")
        if choice == "1":
            inventory.pop(searchRes[1]-1)
            print("--> Delete successful")
    else:
        print("--> Product not found!")


def view_statistics():
    # TODO: print total products, total quantity, total value, categories.
    total = 0
    value = 0
    quantity = 0
    for i in inventory:
        value += i["price"]
        quantity += i["quantity"]
        total += 1
    print(f"Total products = {total:<5} Total value = {value:<15} Total quantity = {quantity:<10}")
    print(f"Categories: {categories}")
