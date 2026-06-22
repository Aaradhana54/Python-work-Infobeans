'''
Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km
'''
speed=int(input("Enter speed km/hr = "))
hours,min=map(int,input("Enter time in hours and min = ").split())
inMin=hours*60+min
Total_time=inMin/60
print("Total time = ",Total_time)
print("Distance = ",Total_time*2.5)





