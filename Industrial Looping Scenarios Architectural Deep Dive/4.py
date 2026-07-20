"""
Question 04: Space Launch Reverse Countdown

Scenario & Concept:
Satellite launch se pehle system reverse timing calculate karta hai.

Problem Statement:
Negative step value ka use karte hue range generator design karein.
Timer value ko decrement order mein zero tak navigate karein.

Input Format:
count = 5

Output Format:
T-minus 5
T-minus 4
T-minus 3
T-minus 2
T-minus 1
Blast Off!

Constraints:
- Negative step parameter in range(start, stop, step)
  must be carefully utilized.
"""

# Input
count = 5

# Reverse countdown
for i in range(count, 0, -1):
    print("T-minus", i)

# Final message
print("Blast Off!")