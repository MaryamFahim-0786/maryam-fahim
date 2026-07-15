# Question 10: Aapke paas daily tasks ki list hai:
# tasks = ["Check Backup", "Update OS", "Send Report"].
# Ek critical security bug report hota hai. Is task "Fix Critical Bug" ko
# task list ke bilkul shuru mein (index 0) par insert karein aur updated list print karein.

# Daily tasks ki list 
tasks = ["Check Backup", "Update OS", "Send Report"]

# "Fix Critical Bug" task to index 0 insert
tasks.insert(0, "Fix Critical Bug")

# Updated task list print 
print("Updated task list:", tasks)