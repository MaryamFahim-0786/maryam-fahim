"""
Question 01: The Spotify Track Repeater

Scenario & Concept:
Spotify par jab user repeat mode active karta hai, to gaana baar-baar chalta hai.
Hum ek program design karenge jo user ke favorite song ko unki demand ke mutabiq repeat kare.

Problem Statement:
Ek input variable song_name aur repeat limit N lein.
while loop ka istemal karte hue gaane ko sequentially print karein
aur sath loop count bhi display karein.

Input Format:
song_name = "Soul Light"
N = 3

Output Format:
Playing: Soul Light (Repeat Count: 1)
Playing: Soul Light (Repeat Count: 2)
Playing: Soul Light (Repeat Count: 3)

Constraints:
- N must be positive.
- Program must handle indentation correctly using 4 spaces or tab.
"""

# Input
song_name = input("Enter song name: ")
N = int(input("Enter repeat limit: "))

# Counter
count = 1

# While loop
while count <= N:
    print("Playing:", song_name, "(Repeat Count:", count, ")")
    count += 1