'''
3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5'''
n=int(input("Enter number: "))
first=None
if n==0:
  smallest=n
while n>0:
   digit=n%10
   l=len(str(n))
   if(l==1):
      print("First digit",digit)
   n=n//10
   
   
