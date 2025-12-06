def nonNegativeAverage(arr):
    noOfNonNegative = 0
    sumOfNonNegative = 0

    for n in arr:
        if n >= 0:
            sumOfNonNegative += n
            noOfNonNegative = noOfNonNegative+1
    
    if noOfNonNegative == 0:
        return 0
    
    avgOfNonNegative = sumOfNonNegative / noOfNonNegative
    return avgOfNonNegative


print(nonNegativeAverage([-12, 8, -7, 6, 12, -9, 14]))