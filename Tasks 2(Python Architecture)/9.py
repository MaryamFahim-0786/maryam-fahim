# Question 09: Aapki system monitoring script ne database queries ki latencies
# (in milliseconds) save ki hain. Built-in functions ka use karke sub se fast
# query execution time (minimum value) aur sub se slow query execution time
# (maximum value) find karke print karein.

# Database query latencies  list 
latencies = [120, 250, 90, 300, 150]

# Minimum latency (fastest query) find 
fastest_query = min(latencies)

# Maximum latency (slowest query) find 
slowest_query = max(latencies)

# Fastest aur slowest query execution time print 
print("Fastest query execution time:", fastest_query, "ms")
print("Slowest query execution time:", slowest_query, "ms")