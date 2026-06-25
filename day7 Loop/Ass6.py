'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong'''
n=int(input("Enter a Number: "))
temp=n
sum=0
rev=0
length=len(str(n))
'''
for i in range(len(str(n))):
   digit=n%10
   sum+=digit**length
   n=n//10

     '''
while n>0:
   digit=n%10
   sum+=digit**length
   n=n//10
print(sum)
if(sum==temp):
   print("Armstrong Number")
else:
   print("Not a Armstrong number")
     