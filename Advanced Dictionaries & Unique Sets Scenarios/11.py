"""
Question 11: Banned IP Controller (Remove Method)

Firewall protection system ke paas block access sets hain.

SETS

blocked_ips = {
    "192.168.1.1",
    "10.0.0.1"
}

Agar aik IP ko safe declare kar diya jaye,
to use set se .remove() kaise karenge?

Code likh kar update check karein.
"""

# Solution

blocked_ips = {
    "192.168.1.1",
    "10.0.0.1"
}

# Remove safe IP
blocked_ips.remove("192.168.1.1")

# Print updated set
print(blocked_ips)