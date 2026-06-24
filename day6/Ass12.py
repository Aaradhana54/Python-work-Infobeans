'''
12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680
'''
amount=int(input("Enter bill amount: "))
if amount<=1000:
   gst=amount*0.5
   print("Final Bill Amount:",amount+gst)         
elif amount>=1001 and amount<=5000:
    gst=amount*0.12
    if amount>3000:
       print("Final Bill Amount:",amount+gst+200)                           
else:
   gst=amount*0.18
   print("Final Bill Amount:",amount+gst+200) 
      
       
   
  