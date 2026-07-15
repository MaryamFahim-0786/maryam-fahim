# Question: Aapne security reasons ke liye server connectivity details ek tuple
# mein store ki hain:
# server_config = ("192.168.1.1", 8080).
# Ek test code likhein jo is configuration ke port number (index 1) ko update
# karne ki koshish kare, taake check kiya ja sake ke system data edit to nahi ho raha
# (TypeError inspect karein).

# Server configuration store in  tuple  
server_config = ("192.168.1.1", 8080)

# Tuple ke port number (index 1) update  
try:
    server_config[1] = 9090

# if tuple modify to  generate TypeError
except TypeError:
    print("TypeError: Tuple values cannot be changed")

# Original tuple print 
print("Server configuration:", server_config)