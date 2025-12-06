def decrementList(arr):
    #code here
    newArr = []
    for n in arr:
        decrementValue = n-1
        newArr.append(decrementValue)
    return newArr

print(decrementList([54, 43, 2, 1, 5]))