'''
Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
'''
amount=int(input("Enter Amount: "))
hun=amount//100
hunrem=amount%100
fifty=hunrem//50
fiftyrem=hunrem%50
ten=fiftyrem//10
print(f"₹100 x {hun}\n₹50 x {fifty}\n ₹10 x {ten}")
