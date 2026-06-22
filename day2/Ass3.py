''' Assignment 3: Split the Bill
========================================

You and your friends went out to eat. The bill was quite high and you want to split it evenly.

Write a Python program that:
- Accepts the total bill amount.
- Accepts the number of friends.
- Displays how much each person should pay.

Example:
Total bill = 1250
Friends = 5
Each should pay = 250.0
'''
totalbill=int(input("Enter Total bill: "))
friends=int(input("Enter the total number of friends: "))
pay=totalbill/friends
print(f"Total bill = {totalbill}")
print(f"Friends = {friends}")
print(f"Each should pay= {pay}")