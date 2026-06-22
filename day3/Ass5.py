'''
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
------------------------------------------------------------
'''
eng,hindi,math=map(int,input("Enter marks of english hindi and maths: ").split(","))
print(eng,hindi,math,sep=",")
avg=(eng+hindi+math)/3
print(f"Average = {avg} ")