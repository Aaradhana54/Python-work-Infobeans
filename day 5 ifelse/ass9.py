'''
9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books'''

active=input("Membership active (yes/no):")
booksissued=int(input("Enter number of book issued :"))
if active.lower()=="yes":
   print("Entry allowed")
   if booksissued < 3:
       print("Can issue more books")
   else:
       print("Can not issue more books")
else:
    print("Enter not allowed")