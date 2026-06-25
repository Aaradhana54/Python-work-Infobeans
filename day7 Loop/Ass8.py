'''
8.Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3
'''
n=int(input("Enter a Number: "))
count=0
length=len(str(n))
'''
for i in range(len(str(n))):
   digit=n%10
   if(digit%2!=0):
      count+=1
   n=n//10

     '''
while n>0:
   digit=n%10
   if(digit%2!=0):
      count+=1
   n=n//10
print(count)
     