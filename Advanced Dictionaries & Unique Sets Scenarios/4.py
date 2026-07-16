"""
Question 04: Salary Record Eraser (Pop Method)

HR Database mein privacy maintain rakhne ke liye
employee ki dictionary

employee = {
    "name": "Sarah",
    "role": "Designer",
    "salary": 95000
}

Se salary key-value pair ko permanent delete karna hai.

.pop() method ka use karke isay remove karein
aur updated dictionary print karein.
"""

# Solution

employee = {
    "name": "Sarah",
    "role": "Designer",
    "salary": 95000
}
# extra
employee["department"]="IT"


# Remove salary
employee.pop("salary")

# Print updated dictionary
print(employee)