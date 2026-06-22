'''
Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
----------------------------------------------------------------
'''
amount=int(input("Enter amount: "))
dis=amount//10
final=amount-dis
print(f"Discount = {dis} \n Final = {final}")
