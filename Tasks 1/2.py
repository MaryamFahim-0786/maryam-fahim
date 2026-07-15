'''
Question 02: Banned Keyword Check (Naming Rules)

Aap user roles save karne ke liye variable ka naam
for = "Admin" rakhna chahte hain.
Python is par error kyun deta hai,
aur Python ke "reserved words/keywords"
ka variable naming se kya talluq hai?
'''

# Wrong (This  will always give SyntaxError)
# for = "Admin"

# Correct variable name
user_role = "Admin"

# Print the value
print(user_role)