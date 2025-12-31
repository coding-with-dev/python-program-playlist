def checkArmstrongNumber(num):
    power = len(num)

    numSum = 0
    for i in num:
        numSum += int(i) ** power
    
    if(str(numSum) == num):
        print("Is a armstrong number")
    else:
        print("Is not a armstrong number")

num = input("Enter any number to check armstrong number : ")
checkArmstrongNumber(num)