# Mini Inventory Manager

A command-line inventory management program for a small store. It is designed
as a single practical exercise that combines core Python fundamentals —
variables & data types, lists/dicts/tuples/sets, `for`/`while` loops,
`if`/`else`, functions, file I/O, and `try`/`except` — instead of practicing
them in isolation.

## Overview

The program runs as a menu that loops in the terminal until the user chooses
"Exit". Inventory data is saved to a file so nothing is lost when the program
closes, and is reloaded automatically the next time it starts.

## Menu

```
===== INVENTORY MANAGEMENT =====
1. Add product
2. View all inventory
3. Search product by name
4. Update quantity/price
5. Delete product
6. View inventory statistics
7. NumPy analysis
0. Exit (auto-saves before exiting)
```

## Features

1. **Add product** — add a new product to the inventory.
2. **View all inventory** — list every product currently in stock.
3. **Search product by name** — find a product and report whether it exists.
4. **Update quantity/price** — edit an existing product's quantity or price.
5. **Delete product** — remove a product from the inventory.
6. **View inventory statistics** — summary stats over the current inventory.
7. **NumPy analysis** — a submenu of NumPy practice exercises that run
   against the real inventory data. See [NUMPY_EXERCISES.md](NUMPY_EXERCISES.md).
0. **Exit** — save the inventory and end the program.

## Project structure

- [main.py](main.py) — thin entry point (`python main.py` to run).
- [menu.py](menu.py) — the menu loop and dispatch to each feature.
- [inventory_operations.py](inventory_operations.py) — the actual
  CRUD/business logic (load/save, add/search/update/delete, statistics).
- [numpy_exercises.py](numpy_exercises.py) — the NumPy practice module
  (menu option 7), also runnable standalone.

For suggested data structures, the file format, and error-handling
requirements, see [NOTES.md](NOTES.md).
