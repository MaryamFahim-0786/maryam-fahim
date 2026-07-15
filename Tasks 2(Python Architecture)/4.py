'''
Question 04: ATM Cash Withdrawal Limit

CONDITIONALS

Ek ATM transaction check system likhein
jahan user ka current balance
balance = 15000 set ho.

User se withdraw hone wala amount input lein.
Agar amount balance ke barabar ya usse kam hai,
to balance se deduct karke updated balance dikhayein,
warna "Insufficient Funds" print karein.
'''

# Initial balance
balance = 15000

# Take withdrawal amount from user
amount = int(input("Enter withdrawal amount: "))

# Check balance
if amount <= balance:
    balance = balance - amount
    print("Updated Balance:", balance)
else:
    print("Insufficient Funds")