"""
Question 07: Profile Merger (Update Method)

Aap ke paas do alag systems ka customer data hai.

DICTIONARIES

basic_info = {
    "name": "Hamza"
}

professional_info = {
    "role": "AI Specialist"
}

.update() method ka use karte hue
professional_info ko basic_info ki dictionary mein
merge karein aur check karein.
"""

# Solution

basic_info = {
    "name": "Hamza"
}

professional_info = {
    "role": "AI Specialist"
}

# Merge dictionaries
basic_info.update(professional_info)

# Print updated dictionary
print(basic_info)