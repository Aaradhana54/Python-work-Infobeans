'''
Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h
'''
Distance1=int(input("Enter distance1: "))
Time1=int(input("Enter time1: "))
Distance2=int(input("Enter distance2: "))
Time2=int(input("Enter time2: "))
print("Distance1 =",Distance1)
print("Time1 = ",Time1)
print("Distance2 =",Distance2)
speed1=Distance1//Time1
speed2=Distance2//Time2
print("Average Speed = ",(speed1+speed2)//2,"km/h")