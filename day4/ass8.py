'''
Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0
'''
pri,rate,time=map(int,input("Enter principal rate and time: ").split())
amount=pri*(1+rate/100)**time
print(f"Amount after interest  = {round(amount,2)}")