"""
Question 09: Unique Website Traffic (Duplicates Removal)

Aapke analytics server par dynamic IPs se requests aayi hain.

SETS

traffic = ["IP-1", "IP-2", "IP-1", "IP-3", "IP-2"]

Is list ko set mein convert karein taake
duplicate IPs khud-b-khud delete ho jayein
aur unique IPs print ho sakein.
"""

# Solution

traffic = ["IP-1", "IP-2", "IP-1", "IP-3", "IP-2"]

# Convert list to set
unique_ips = set(traffic)

# Print unique IPs
print(unique_ips)