'''
Question 02: Automated Marks Grading

CONDITIONALS

Ek school portal ke liye automatic grading
program banayein jo student ke exam marks
(0 to 100) input le.

Agar marks 90 ya usse zyada hon to "Grade A",
agar 80 se 89 ke darmiyan hon to "Grade B",
aur baqi tamam marks par "Grade C" print kare.
'''

# Take marks from user
marks = int(input("Enter your marks: "))

# Check grade
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")