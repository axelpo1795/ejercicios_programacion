def is_prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

def get_prime_nums(num_list):
    prime_numbers = []
    for num in num_list:
        if is_prime_num(num):
            prime_numbers.append(num)
    return prime_numbers

print(get_prime_nums([1, 4, 6, 7, 13, 9, 67]))
