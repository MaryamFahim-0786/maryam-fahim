"""
Question 10: E-Commerce Inventory Dispatcher

Scenario & Concept:
Warehouse automation mein dispatch items ke lists ko
systematically iterate kiya jata hai.

Problem Statement:
Ek custom collection array (list) banayein aur use for loop
se traverse kar ke packaging labels print karein.

Input Format:
item_list = ["Item-A", "Item-B", "Item-C"]

Output Format:
Dispatched: Item-A
Dispatched: Item-B
Dispatched: Item-C

Constraints:
- Do not use manually hard-coded indexes.
- Utilize dynamic variable assignment of the loop container.
"""

# Item list
item_list = ["Item-A", "Item-B", "Item-C"]

# For loop
for item in item_list:
    print("Dispatched:", item)