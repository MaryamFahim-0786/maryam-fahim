"""
Question 13: Skill Finder (Set Intersection)

Two developers ke tech stacks sets mein define hain.

SETS

dev1 = {"Python", "SQL", "HTML"}

dev2 = {"Java", "Python", "CSS"}

Sets ke intersection operator/method ka use karte hue
unki common skills find karein bina kisi
dynamic check loop ke.
"""

# Solution

dev1 = {"Python", "SQL", "HTML"}
dev2 = {"Java", "Python", "CSS"}

# Find common skills
common_skills = dev1.intersection(dev2)

# Print common skills
print(common_skills)