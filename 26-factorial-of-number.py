import math
def calculate_fact(num):
    if(num == 1):
        return 1
    else: 
        return num*calculate_fact(num - 1)
    
num = int(input("Enter a number: "))
print("Calculated using Custom Function - ", calculate_fact(num))
print("Calculated using Inbuilt Function - ", math.factorial(num))