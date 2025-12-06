def pos(n):
    for i in range((n-1), -1, -1):
        print(i)        
    
def neg(n):
    for i in range(n, 1, 1):
        print(i)

n = int(input("Enter Number : "))

if n == 0:
    print("already Zero")
elif n > 0:
    pos(n)
else:
    neg(n)