"""
Question 03: Automated Port Pinger

Scenario & Concept:
Network engineer ko database servers check karne ke liye
servers range scan karni hoti hai.

Problem Statement:
range() function ka use karte hue port boundaries scan karein.
Server nodes start index aur stop index input le kar
sequential traversal perform karein.

Input Format:
start = 10
stop = 14

Output Format:
Scanning Server Node 10
Scanning Server Node 11
Scanning Server Node 12
Scanning Server Node 13

Constraints:
- Last boundary (stop) exclusive hoti hai.
- Program ko user requirements ke mutabiq adjustment karna chahiye.
"""

# Input
start = int(input("Enter start node: "))
stop = int(input("Enter stop node: "))

# For loop
for i in range(start, stop):
    print("Scanning Server Node", i)