"""
Question 15: Network Monitor Delay Scanner

Scenario & Concept:
Network monitor har sensor node ko check karne ke baad
exact 1 second ka gap delay rakhta hai taake resources free rahin.

Problem Statement:
Python standard module utility importing system seekhein.
Loop state transition delays integrate karne ke liye
library configuration perform karein.

Input Format:
Loop configuration bounds.

Output Format:
Output lines displaying with a strict sequential delay pattern.

Constraints:
- Code execution flow must pause precisely for
  the specified duration on each iteration.
"""

# Import time module
import time

# Loop
for i in range(1, 6):
    print("Checking Sensor Node:", i)
    time.sleep(1)    # Delay of 1 second

print("All Sensor Nodes Checked.")