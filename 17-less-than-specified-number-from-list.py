def lessThan(arr, k):
    #code here
    ans = []
    for n in arr:
        if n < k:
            ans.append(n)
    return ans

print(lessThan([54, 43, 2, 1, 5], 6))