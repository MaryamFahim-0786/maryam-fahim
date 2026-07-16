"""
Question 02: Contact Book Phone Update (Mutability)

Ek student contact portal par student ka mobile number change karna hai.

DICTIONARIES

student_contact = {
    "Ali": "0300-1234567"
}

Dictionary mein Ali ka contact number update karke
"0300-9999999" karein aur check karein ke kya value change ho gayi hai.
"""

# Solution

student_contact = {
    "Ali": "0300-1234567"
}

# Update contact number
student_contact["Ali"] = "0300-9999999"

# Check updated value
print(student_contact["Ali"])