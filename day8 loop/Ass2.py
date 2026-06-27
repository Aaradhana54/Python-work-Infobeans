'''
2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2'''
n=int(input("Enter number: "))
smallest=9
if n==0:
  smallest=n
while n>0:
   digit=n%10
   if smallest>digit:
      smallest=digit
   n=n//10
print("Smallest Digit:",smallest)