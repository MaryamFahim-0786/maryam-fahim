# Question 12: Ek text editor user ke operations ko track kar raha hai:
# actions = ["Type 'Hello'", "Make Bold", "Insert Table"].
# User "Undo" button dabata hai. List method use karke action list ke
# aakhri element ko nikalhein (pop karein) aur print karein ke kaunsa action remove hua hai.

# User actions  list 
actions = ["Type 'Hello'", "Make Bold", "Insert Table"]

# Last action remove  using pop() method
removed_action = actions.pop()

# Remove  action print 
print("Removed action:", removed_action)

# Updated actions list print 
print("Updated actions list:", actions)