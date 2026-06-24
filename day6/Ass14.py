'''
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
'''

category=input("Enter course category(programming,design or Marketing): ")
type=input("Enter user type(student,working professional,others): ")
if category.lower()=="programming":
   if type.lower()=="student":
      fee=5000*0.2
      print("Final Course Fee: ",5000-fee)
   elif type.lower()=="working professionals":
      fee=5000*0.1
      print("Final Course Fee: ",5000-fee)
   else:
       print("Final Corse Fee:5000 Rs")
               
elif category.lower()=="design":
   if type.lower()=="student":
      fee=4000*0.2
      print("Final Course Fee: ",4000-fee)
   elif type.lower()=="working professionals":
      fee=4000*0.1
      print("Final Course Fee: ",4000-fee)
   else:
       print("Final Corse Fee:4000 Rs")
else:
   if type.lower()=="student":
      fee=3000*0.2
      print("Final Course Fee: ",3000-fee)
   elif type.lower()=="working professionals":
      fee=3000*0.1
      print("Final Course Fee: ",3000-fee)
   else:
       print("Final Corse Fee:3000 Rs")
 
      
       
   
  