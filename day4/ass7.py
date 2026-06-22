'''
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67

'''
total=int(input("Enter total runs : "))
overs,balls=map(int,input("Enter total overs : ").split("."))
balls=overs*6+balls
print("Total balls = ",balls)
print("Run rate = ",round(total/(balls/6),2))