'''
Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
'''
n=int(input("Enter a Number: "))
count=0
length=len(str(n))
bool=True
'''
for i in range(length):
   digit=n%10
   if(digit%2!=0):
      bool=False
   n=n//10

     '''
while n>0:
   digit=n%10
   if(digit%2!=0):
      bool=False
   n=n//10
  
if(bool):
   print("All Digits are Even")
else:
   print("All Digits are not Even")
     