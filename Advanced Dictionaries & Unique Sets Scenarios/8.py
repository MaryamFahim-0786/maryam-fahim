"""
Question 08: Duplicate Key Bug (Overwrite Behavior)

DICTIONARIES

Agar aap galti se ek hi student dictionary mein
same key do dafa write kar dete hain, jaise

student_data = {
    "name": "Asad",
    "age": 22,
    "name": "Bilal"
}

Jab aap student_data["name"] ko print karenge,
to console par kya output aayegi aur Python ka
back-end algorithm is situation mein kis value ko
priority deta hai?
"""

# Solution

student_data = {
    "name": "Asad",
    "age": 22,
    "name": "Bilal",
    "name": "Maryam"
}

print(student_data["name"])