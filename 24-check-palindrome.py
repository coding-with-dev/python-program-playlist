def isPalindrome(s):
    #code here
    s = s.lower()
    reversedString = s[::-1]

    return s == reversedString
    
print(isPalindrome("nlllsss"))