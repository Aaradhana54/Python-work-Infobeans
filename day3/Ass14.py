'''
Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
'''
Cost_Price = int(input("Enter Cost price : "))
Selling_Price=int(input("Enter Selling Price: "))
print("Cost Price = ",Cost_Price)
print("Selling Price = ",Selling_Price)
profit=Selling_Price-Cost_Price
profit_per=(profit/Cost_Price)*100
print("Profit =",profit)
print("profit_per = ",profit_per)
