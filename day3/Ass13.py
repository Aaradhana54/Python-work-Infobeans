'''
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0
'''
pri,rate,time=map(int,input("Enter principal rate and time: ").split())
amount=pri*(1+rate/100)**time
ci=amount-pri
print(f"Amount = {round(amount,2)}\n Compound Interest = {round(ci,2)}")