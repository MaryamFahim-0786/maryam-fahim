# Question 14: Aapko server ka deployment mode "Production" aik single-value
# tuple mein store karna hai. Ek aisa code likhein jo isay sahi tarike se
# single-item tuple banaye (bina string treat kiye) aur user ko iska proper
# data type check karke print karwaye.

# Single-element tuple  (comma is imp)
deployment_mode = ("Production",)

# To chk tuple type
print("Data type:", type(deployment_mode))

# To print tuple value
print("Deployment mode:", deployment_mode)