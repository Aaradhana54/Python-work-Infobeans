'''
Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
'''
total,obtaines=map(int,input("Enter total marks and obtained marks :").split())
print(f"Total = {total}\n Obtained={obtaines}")
per=(obtaines/total)*100
print(f"Percentage = {per}")