'''
Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75

---
'''
amount=int(input("Enter total amount: "))
gst=int(input("Enter Gst: "))
service_charge=int(input("Enter Service Charge: "))
numOfFrnds=int(input("Enter Number of friends: "))
gstprice=amount*gst/100
serviceprice=amount*service_charge/100
finalbill=amount+gstprice+serviceprice
print("Final Bill = ",finalbill)
print("Each Person Pays = ",finalbill/numOfFrnds)
