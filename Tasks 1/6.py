'''
Question 06: Type Error in Logging (Concatenation)

Ek developer server logging ke liye code likhta hai:
print("Active connections: " + 15)

Python is par error kyun dega,
aur isay sahi tarike se print karne ke
do tareeqe kya hain?
'''

# Method 1: Convert integer to string
print("Active connections: " + str(15))

# Method 2: Use comma
print("Active connections:", 15)