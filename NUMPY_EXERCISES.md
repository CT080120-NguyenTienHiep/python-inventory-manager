# NumPy Practice

10 exercises to practice NumPy fundamentals — arrays, indexing/slicing,
element-wise operations, reshape, and axis-wise statistics — using the
**real inventory data** from the main CLI project (`inventory_operations.py`
/ `inventory.csv`), instead of hardcoded sample arrays.

No solutions are included on purpose. Each exercise is its own function
in [numpy_exercises.py](numpy_exercises.py), named after what it does
(e.g. `slice_first_and_last_names`, `reshape_prices_by_category`) —
write your code inside the matching function. Run them through a
submenu, either way:

- standalone: `python numpy_exercises.py`
- from the CLI: `python main.py` → option **7. NumPy analysis**

Both open the same submenu, listing exercises 1–9 plus "0. Back". Work
through them **in order** — later exercises reuse arrays built by earlier
ones, shared as module-level variables (`names`, `prices`, `quantities`,
`prices_by_category`) rather than passed as parameters.

## Setup

Loading the real inventory isn't one of the numbered exercises — it's a
mandatory first step, `build_arrays_from_inventory()`, that
`run_numpy_analysis()` always calls once before showing the submenu (so
`names`/`prices`/`quantities` are never `None` when an exercise uses
them). It goes through `inventory_operations.py`'s `load_inventory()`.
That function doesn't return the data — it stores it in its own
module-level global `inventory` variable — so it needs to be called and
then that global read out:

```python
import inventory_operations as ops
ops.load_inventory()
inventory = ops.inventory
```

`inventory` is the same list of dicts the CLI project uses, with `price`
and `quantity` already stored as `int` (`load_inventory` parses them
itself).

## Exercises

1. Use slicing to print the first 5 and the last 5 product names.
2. Use boolean indexing to get the names of products with `quantity < 10`
   (a low-stock alert).
3. Compute the inventory value of every product (`prices * quantities`),
   then print the grand total value of the whole shop with `np.sum()`.
4. Find the index and name of the most expensive product using
   `np.argmax`.
5. Reshape `prices` into a 2-D matrix of shape `(5, 10)` — the current
   `inventory.csv` has 5 categories with 10 products each, in that order.
   Store it as `prices_by_category`. (If you've added/removed products
   via the CLI since then, adjust the shape to match the current total.)
6. Compute the total price sum per category — `np.sum` with the right
   axis.
7. Compute the average price per category — `np.mean` with axis.
8. Compute the standard deviation of prices within each category
   (`np.std` with axis) — which category has the most price variation?
9. Flatten `prices_by_category` back into a 1-D array with `.flatten()`,
   and confirm it's identical to the original `prices` array (e.g.
   `np.array_equal`).
