def digit_sum(num):
    total = 0

    while num > 0:
        total += num % 10 
        num //= 10 #removes the last digit 

    return total

def is_composite(num):
    if num < 4:
        return False

    for i in range(2, int(num ** 0.5) +1):
        if num % i == 0:
            return True

    return False

def find_number(n):
    candidate = n+1

    while True:
        if is_composite(candidate) and digit_sum(candidate)%2 == 1:
            return candidate
        candidate += 1
        


n = int(input())
print(find_number(n))