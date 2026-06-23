'''
10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
marks ≥ 40 Eligible for certificate
'''

marks,attendence=map(int,input("Enter marks and Attendence: ").split())
if marks >= 40:
   print("Pass")
if attendence >= 75:
   print("Eligible for certificate")