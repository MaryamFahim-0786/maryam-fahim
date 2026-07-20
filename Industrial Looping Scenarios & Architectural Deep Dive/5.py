"""
Question 05: Even-Numbered Package Sorter

Scenario & Concept:
Industrial factory line par machinery ko odd aur even batch numbers
alag karne hote hain.

Problem Statement:
1 se 50 ke darmiyan continuous list traverse karein.
Modulo operator (%) ka use karke check karein ke kaunsa item
strictly divisible by 2 hai aur unhein separate display karein.

Input Format:
Numbers from 1 to 50

Output Format:
Even Batch Processed: 2
Even Batch Processed: 4
...
Even Batch Processed: 50

Constraints:
- Do not use hard-coded lists.
- Calculate dynamically using modulo check inside the loop.
"""

# Starting number
num = 1

# While loop
while num <= 50:
    if num % 2 == 0:
        print("Even Batch Processed:", num)
    num += 1