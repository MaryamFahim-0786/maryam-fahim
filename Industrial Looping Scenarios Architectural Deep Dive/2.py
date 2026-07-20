"""
Question 02: Bruteforce Lockout Guard

Scenario & Concept:
Mobile ya system authentication mein 3 wrong attempts ke baad
login freeze ho jata hai. Agar loop counter increment na ho,
to infinite check bug aa jata hai.

Problem Statement:
Ek password verification mechanism design karein.
Loop ke andar variable state track karein.
Agar user wrong input daale to warning display karein
aur maximum limits hit hone par lockout print karein.

Input Format:
User inputs wrong keys 3 times consecutively.

Output Format:
Login Attempt 1 failed.
Login Attempt 2 failed.
Login Attempt 3 failed. System locked.

Constraints:
- Avoid infinite loop by properly incrementing loop counter inside the block.
"""

# Correct password
correct_password = "maryam123"

# Counter
attempts = 1

# While loop
while attempts <= 3:
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful!")
        break
    else:
        if attempts == 3:
            print("Login Attempt", attempts, "failed. System locked.")
        else:
            print("Login Attempt", attempts, "failed.")

    attempts += 1