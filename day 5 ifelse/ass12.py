'''
2. An e-commerce website provides discounts based on the cart value and user type.
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000,
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise,
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium

Output:
Final Amount = 4800
'''

cartValue=int(input("Enter Cart Value : "))
userType=input("Enter user type (premium or regular):")
if(cartValue >= 5000):
   if userType.lower() == "premium":
      amount=cartValue*0.2
      print("Final Amount = ",cartValue-amount)
   else:
      amount=cartValue*0.1
      print("Final Amount = ",cartValue-amount)
else:
     if cartValue >= 2000:
        amount=cartValue*0.05
        print("Final Amount = ",cartValue-amount)
     else:
         print("No discount applied")
