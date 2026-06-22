'''
Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
'''
hours=int(input("Enter hours: "))
min=int(input("Enter Minutes: "))
sec=int(input("Enter Seconds: "))
total_sec=(hours*3600)+(min*60)+sec
print("Total Seconds = ",total_sec)

