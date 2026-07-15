'''
Question 07: Pizza Area Calculator (Formula Assignment)

Ek online pizza delivery app ke liye,
user se pizza ka diameter input lein.
Area = 3.14 × (diameter / 2)^2

Input ko float mein typecast karein
kyunki input string return karta hai.
'''

# Take input from user
diameter = float(input("Enter pizza diameter: "))

# Calculate area
area = 3.14 * (diameter / 2) ** 2

# Print result
print("Pizza Area =", area)