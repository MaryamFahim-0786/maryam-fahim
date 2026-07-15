'''
Question 01: Smart Traffic Control System

CONDITIONALS

Ek traffic signal automation script likhein
jo user se light ka current color
("Red", "Yellow", "Green") as input le.

Agar light "Red" ho to "Stop your vehicle",
agar "Yellow" ho to "Slow Down",
aur agar "Green" ho to "Go" print kare.
'''

# Take input from user
light = input("Enter traffic light color: ")

# Check the traffic light color
if light == "Red":
    print("Stop your vehicle")
elif light == "Yellow":
    print("Slow Down")
elif light == "Green":
    print("Go")
else:
    print("Invalid traffic light color")