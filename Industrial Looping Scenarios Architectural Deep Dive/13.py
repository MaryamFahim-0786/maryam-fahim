"""
Question 13: Dynamic Invoice Ledger Generator

Scenario & Concept:
Pricing database ko sequential multiplier multiplication logs
generate karne hote hain.

Problem Statement:
Ek product factor key value N ke liye formatted billing table
(1 se 10 multiplication steps) print karein.

Input Format:
N = 3

Output Format:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 10 = 30

Constraints:
- Layout must strictly follow the multiplication logic
  using formatted evaluation.
"""

# Input
N = int(input("Enter a number: "))

# Multiplier
i = 1

# While loop
while i <= 10:
    print(N, "x", i, "=", N * i)
    i += 1