'''
Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0
'''
distance,mileage,petrolprice=map(int,input("Enter distance,mileage,petrolprice: ").split())
petrol_used=distance/mileage
cost=petrol_used*petrolprice
print("Petrol Used = ",petrol_used)
print("Cost =",cost)

