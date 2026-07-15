# Question 15: Ek server security log database access sessions ko store karta hai:
# access_logs = (101, 105, 101, 102, 101, 108, 105).
# Tuple methods ka use karke check karein ke User ID 101 ne kitni dafa
# database access kiya hai, aur User ID 102 pehli dafa kis index position par logged hai.

# To store tuple in Server access logs 
access_logs = (101, 105, 101, 102, 101, 108, 105)

# Find User ID 101 access count  using count() method
user_101_count = access_logs.count(101)

# Find User ID 102 first index position  using index() method
user_102_index = access_logs.index(102)

# Results print 
print("User ID 101 accessed database:", user_101_count, "times")
print("User ID 102 first logged at index:", user_102_index)