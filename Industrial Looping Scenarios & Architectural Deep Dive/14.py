"""
Question 14: Infinite Loop Bug Investigator

Scenario & Concept:
Debugging systems mein code review team logic failures trace karti hai
jahan variables state mismatch hoti hai.

Problem Statement:
Code ka dry run process trace karein.
Check karein ke looping block ki variables state kis point par
exit condition validate nahi kar paati.

Input Format:
Code script displaying variable limits and conditions
lacking incrementing update operations.

Output Format:
Log trace file showing logic checkpoints.

Constraints:
- Must perform manual state variable checking.
- Ensure increment/decrement operation is present
  to avoid infinite execution loop.
"""

# Variable
count = 1

# While loop
while count <= 5:
    print("Current Count:", count)
    count += 1      # Increment to avoid infinite loop

print("Loop Ended Successfully")