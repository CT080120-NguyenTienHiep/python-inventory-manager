# Implementation Notes

## Suggested data structures

*(this is the part meant to practice list / dict / tuple / set)*

- Each product is a `dict`: `{"name": str, "category": str, "price": float, "quantity": int}`
- The whole inventory is a `list` of these dicts: `inventory = [...]`
- Categories must not be duplicated — keep them in a `set`, updated every
  time a new product is added
- The "find product" function should return a `tuple` `(found: bool, index: int)`,
  so the caller knows both whether the product was found and its position,
  in order to edit or delete it

## File I/O requirements

- Persist data as plain text, one product per line, comma-separated:
  `name,category,price,quantity`
- **On startup, the program automatically loads the data file (e.g.
  `inventory.csv`) into the `inventory` list before the menu is shown** —
  this happens unconditionally, not as a menu option the user has to choose
- If the file doesn't exist yet (first run), don't crash — just start with
  an empty inventory instead
- On "Exit": automatically write the entire inventory back to the file
  before the program terminates
- There is no manual "save" menu option — saving only happens automatically
  on exit (and on load at startup)

## Error-handling requirements (`try`/`except`)

*(this is the part that's easy to skip — don't skip it)*

- Non-numeric input for price or quantity must not crash the program —
  print a clear error message and return to the menu
- Searching, updating, or deleting a product that doesn't exist must print
  "Product not found" and not crash
- Reading the file on the very first run, when it doesn't exist yet, must be
  caught as `FileNotFoundError` and not crash

