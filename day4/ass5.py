'''
Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5
'''
monthly,working_days,working_hours_per = map(int,input("Enter monthly salary,Working days,and working hours per day = ").split())
Wd=monthly/working_days
print("Salary per day = ",Wd)
print("Salary per hour = ",Wd/8)