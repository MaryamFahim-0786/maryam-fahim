"""
Question 12: Multi-Hop Node Scanner

Scenario & Concept:
Database backup scripts alternative database nodes scan karti hain
taake performance balanced rahe.

Problem Statement:
range() function mein step configurations define karein.
Start index se lekar stop boundaries tak
alternative points dynamically access karein.

Input Format:
start = 2
stop = 21
step = 10

Output Format:
Scanning alternative Node: 2
Scanning alternative Node: 12

Constraints:
- Step calculations must increment current state index
  by custom step limits.
"""

# Input
start = int(input("Enter start: "))
stop = int(input("Enter stop: "))
step = int(input("Enter step: "))

# For loop
for i in range(start, stop, step):
    print("Scanning alternative Node:", i)