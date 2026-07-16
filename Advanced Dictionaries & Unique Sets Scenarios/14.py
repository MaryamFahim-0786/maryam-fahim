"""
Question 14: Customer Contact Merge (Set Union)

Do marketing campaigns se generate hone wali
unique leads ko merge karna hai.

SETS

leads_a = {
    "ali@mail.com",
    "sara@mail.com"
}

leads_b = {
    "zain@mail.com",
    "sara@mail.com"
}

Set union operation perform karein taake
dono data lists combine ho sakein aur
duplicate "sara@mail.com" clean-up ho jaye.
"""

# Solution

leads_a = {
    "ali@mail.com",
    "sara@mail.com"
}

leads_b = {
    "zain@mail.com",
    "sara@mail.com"
}

# Merge both sets
all_leads = leads_a.union(leads_b)

# Print merged set
print(all_leads)