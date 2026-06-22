'''
Assignment 8: Simple Interest Calculator
========================================

A bank wants to help customers calculate the simple interest on their savings.

Write a Python program that:
- Accepts principal amount, rate of interest, and time (in years) as input.
- Calculates the simple interest using the formula:
  SI = (P × R × T) / 100
- Displays the simple interest.

Example:
Principal = 1000
Rate = 5
Time = 2
Simple Interest = 100.0
'''
prin=int(input("Enter Principal Amount: "))
rate=int(input("Enter Rate Amount: "))
time=int(input("Enter time in years: "))
print(f"Principal = {prin}")
print(f"Rate = {rate}")
print(f"Time = {time}")
SI= (prin*rate*time)/100
print(f"Simple Interest = {SI}")
