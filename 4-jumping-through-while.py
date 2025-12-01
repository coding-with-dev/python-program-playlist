def printIncreasingPower(x):
    start = 1
    squareValue = 1
    while(squareValue <= x):   
        print(squareValue, end=" ")    
        start += 1          
        squareValue = start**2

printIncreasingPower(10)