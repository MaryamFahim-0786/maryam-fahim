"""
Question 06: Subscription Billing Accumulator

Scenario & Concept:
Billing processor ko har customer ki daily usage dynamic pricing
accumulation compute karni hoti hai.

Problem Statement:
N natural items ke pricing indexes ka automated summation
calculator program banayein.

Input Format:
N = 5

Output Format:
Total Invoice Balance: 15
(calculated as 1 + 2 + 3 + 4 + 5 = 15)

Constraints:
- Initialize sum balance as zero before entering accumulator loop.
"""

# Input
N = int(input("Enter the value of N: "))

# Initialize variables
sum = 0
num = 1

# While loop
while num <= N:
    sum = sum + num
    num += 1

# Output
print("Total Invoice Balance:", sum)