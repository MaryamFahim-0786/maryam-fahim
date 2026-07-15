'''
Question 03: Portal Voting Eligibility

CONDITIONALS

Ek government portal par user check karna
chahta hai ke kya woh vote de sakta hai.

User ki age input lein.
Agar age 18 ya usse barhi hai to
"You are eligible to vote" print karein,
warna "You are not eligible to vote" print karein.
'''

# Take age from user
age = int(input("Enter your age: "))

# Check voting eligibility
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")