num_interval = [2, 75]
prime_nums = []
num_last_element = num_interval[-1]

for num in range(num_interval[0], (num_last_element+1)):
    is_prime_num= True
    
    for i in range(2, (num_last_element+1)):
        if(num % i == 0 and num != i):
            is_prime_num = False
    
    if(is_prime_num == True):
        prime_nums.append(num)

print(f"Prime Number from list {num_interval} total count is {len(prime_nums)}")

for prime_num in prime_nums:
    print(prime_num)