"""
Question 01: Product Price Lookup (Basic Access)

Ek online store ke liye product pricing database bana rahe hain.

DICTIONARIES

products = {
    "Laptop": 120000,
    "Mobile": 45000,
    "Headphones": 8000
}

Ek dictionary banayein. Bina kisi loop ke, "Laptop" ki
price ko key ka use karke access karein aur print karein.
"""

# Solution

products = {
    "Laptop": 120000,
    "Mobile": 45000,
    "Headphones": 8000
}

print(products["Laptop"])
print(products["Headphones"])
print(products["Mobile"])