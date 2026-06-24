'''
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''

category=input("Enter vechicle type(Bike,car,bus): ")
parked=int(input("Enter hours parked: "))
if category.lower()=="car":
   if parked>5:
      print("Total Parking Fee:",(parked*20)+100)
   else:
      print("Total Parking Fee:",parked*20)              
elif category.lower()=="bus":
   if parked>5:
      print("Total Parking Fee:",(parked*50)+100)
   else:
      print("Total Parking Fee:",parked*50) 
else:
   if parked>5:
      print("Total Parking Fee:",(parked*10)+100)
   else:
      print("Total Parking Fee:",parked*10) 
  

         
       
   
  