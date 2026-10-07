# Python Week 6 - Error Handling

- `safe_tools.py` - three functions (`safe_divide`, `safe_number`, `get_field`) that use try/except with specific errors so they return a helpful message instead of crashing.
- `unbreakable.py` - a small divider program that keeps asking for input until the user types a valid number, and handles division by zero without crashing.

**Why can an `if` check not catch "abc" on its own?** An `if` check would need to predict every form a valid number can take, such as negative signs, spaces or other formats, and methods like `isdigit()` miss some of them. With `try` / `except`, Python simply attempts `int(text)` and tells us through a `ValueError` if it fails, so every bad input is handled without listing the cases in advance.
