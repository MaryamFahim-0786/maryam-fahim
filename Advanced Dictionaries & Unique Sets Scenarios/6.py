"""
Question 06: Database Fields Auditor (Keys & Values)

Ek user registration table ki details

user_profile = {
    "username": "zain_dev",
    "email": "zain@mail.com",
    "status": "Active"
}

Mein store hain.

.keys() method ka use karke tamam field names
aur .values() method ka use karke unka data
alag se list out karein.
"""

# Solution

user_profile = {
    "username": "zain_dev",
    "email": "zain@mail.com",
    "status": "Active"
}

# Print all keys
print(user_profile.keys())

# Print all values
print(user_profile.values())