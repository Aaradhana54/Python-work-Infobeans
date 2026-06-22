'''
Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2
'''
mark1,mark2,mark3,mark4,mark5 =map(int,input("Enter Marks of 5 subjects: ").split())
total=mark1+mark2+mark3+mark4+mark5
print("Total =",total)
print("Average =",total/5)
print("Percentage =(total/500)*100 ",)