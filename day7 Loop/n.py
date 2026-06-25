a=int(input("Enter no: "))
b=int(input("Enter no: "))
if a<b:
   if a%2==0:
      for i in range(a,b+1,2):
           print(i,end=" ")
   else:
      for i in range(a+1,b+1,2):
           print(i,end=" ")
else:
   if a%2==0:
      for i in range(a-1,b-1,-2):
           print(i,end=" ")
   else:
      for i in range(a,b-1,-2):
           print(i,end=" ") 