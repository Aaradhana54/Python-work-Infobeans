'''
Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000
----------------------------------------------
'''
dailywage,days=map(int,input("Enter dailywages and days : ").split())
salary=dailywage*days
print("Salary = ",salary)