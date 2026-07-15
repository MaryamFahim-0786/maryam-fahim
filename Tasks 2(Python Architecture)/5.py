'''Question 05: E-Commerce Discount Voucher
CONDITIONALS
Ek shopping website ke checkout button par logic lagayein. User se total cart value input lein. Agar cart
value 5000 PKR se zyada hai to total bill par 10% discount apply kar ke discounted total print karein,
warna print karein "No discount applicable".'''


cart_value = int(input("Enter total cart value (PKR): "))

if cart_value > 5000:
    discount = cart_value * 0.10
    discounted_total = cart_value - discount
    
    print("10% discount applied!")
    print("Discounted total:", discounted_total, "PKR")
else:
    print("No discount applicable")