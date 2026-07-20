"""
Question 08: Maintenance Task Skipper

Scenario & Concept:
Periodic task runner servers check karta hai magar maintenance
days par specific banned IDs ya reserved codes skip karne hote hain.

Problem Statement:
continue statement ka logic explore karein.
User targets scan karte waqt targeted anomaly block skip karein
aur baki traversal continue rakhein.

Input Format:
Sequence of nodes up to 5, skipping Node 3.

Output Format:
Scanning Node: 1
Scanning Node: 2
Skipping Maintenance Node 3
Scanning Node: 4
Scanning Node: 5

Constraints:
- The execution block underneath the continue statement
  must skip execution for that single loop turn.
"""

# For loop
for i in range(1, 6):

    if i == 3:
        print("Skipping Maintenance Node 3")
        continue

    print("Scanning Node:", i)