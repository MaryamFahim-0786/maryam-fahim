"""
Question 05: Safe Server Search (Get Method)

Server configuration dictionary

config = {
    "host": "localhost",
    "port": 8080
}

Mein se port number search karna hai.

.get() method ka istemal karke port check karein aur
agar koi aisi key search ki jaye jo dictionary mein
na ho (jaise "username"), to crash hone ke bajaye
safety response check karein.
"""

# Solution

config = {
    "host": "localhost",
    "port": 8080,
    
}

# Get existing key
print(config.get("port"))

# Get non-existing key
print(config.get("username", "Key Not Found"))