'''
Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4

'''
tseconds=int(input("Enter Total Seconds = "))
hours=tseconds//3600
remaining=tseconds%3600
minutes=remaining//60
remaining=remaining%60
print("Hours = ",hours)
print("Minutes = ",minutes)
print("Seconds = ",remaining)

