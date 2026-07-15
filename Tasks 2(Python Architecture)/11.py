# Question 11: Ek active community users ki list hai:
# members = ["ali_dev", "banned_user_10", "sara_ux", "zain_qa"].
# System scan ke baad aapko "banned_user_10" ko remove karna hai.
# Value-based list method use karke use remove karein aur clean list print karein.

# Active community users list 
members = ["ali_dev", "banned_user_10", "sara_ux", "zain_qa"]

# "banned_user_10"  value  through remove 
members.remove("banned_user_10")

# Clean user list print 
print("Updated members list:", members)