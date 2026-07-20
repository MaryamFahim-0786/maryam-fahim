"""
Question 09: Server Overheat Emergency Interrupter

Scenario & Concept:
Server sensor continuous check chalata hai, lekin agar temperature
safe thresholds exceed kare to system crash se bachane ke liye
operation band kiya jata hai.

Problem Statement:
break statement ka practical check implement karein.
Jab loop temperature limits 90 degree touch kare,
to loop instantly break karein aur message print karein.

Input Format:
temperatures = [40, 60, 92, 70]

Output Format:
Current Temperature: 40 C
Current Temperature: 60 C
Danger: 92 C detected! Shutting down system.

Constraints:
- System loop must immediately terminate.
- Control must move outside the loop block on anomaly detection.
"""

# Temperature list
temperatures = [40, 60, 92, 70]

# For loop
for temp in temperatures:

    if temp > 90:
        print("Danger:", temp, "C detected! Shutting down system.")
        break

    print("Current Temperature:", temp, "C")