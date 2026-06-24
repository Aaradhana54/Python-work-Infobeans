'''
4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
'''

subscription=input("Enter subscription: ")  
progress=int(input("Enter progress: "))  
score=int(input("Enter test score: "))

if subscription.lower()=="premium":
   if progress>=80:
      if score >= 70:
           print("Access Status = unlock certificates")
      else:
           print("Access Status = allow retry test")      
   else:
       print("Complete course")   
elif subscription.lower()=="basic":
   if progress>=50:
       print("Access Status = allow limited access")      
   else:
       print("Access Status = lock content") 
else:
    print("Deny acess") 
           
   
  