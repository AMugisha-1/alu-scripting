import importlib

# Load the module dynamically
top_ten_module = importlib.import_module("1-top_ten")

# Call the function
top_ten_module.top_ten("programming")
