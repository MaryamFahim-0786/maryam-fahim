"""
Question 07: UI Separator Pattern Generator

Scenario & Concept:
Mobile apps aur website terminal dashboards ko partition rules
ke liye unique pattern lines print karni hoti hain.

Problem Statement:
String multiplication operator (*) aur numeric incremental state
ka use karke sequential stair shape pattern generate karein.

Input Format:
levels = 4

Output Format:
*
**
***
****

Constraints:
- Max limits are bound by user input variable limit.
"""

# Input
levels = 4

# Counter
n = 1

# While loop
while n <= levels:
    print("*" * n)
    n = n + 1