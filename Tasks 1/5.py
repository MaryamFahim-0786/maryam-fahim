'''
Question 05: Syntax Halt Analysis (Interpreter Behavior)

Aapke code file mein 3 lines hain:

Line 1: print("Starting System...")
Line 2: print("Loading Database (unclosed quote error)
Line 3: print("System Ready!")

Jab aap is program ko run karenge,
to kya Line 1 execute hogi ya program pehle hi ruk jayega?
Python interpreter ke behavior ko samjhayein.
'''

# Line 1
print("Starting System...")

# Line 2 (Syntax Error - Missing closing quote)
print("Loading Database")

# Line 3
print("System Ready!");