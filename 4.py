def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def find_perfect_numbers(limit):
    perfect_numbers = []
    for num in range(2, limit):
        if is_perfect(num):
            perfect_numbers.append(num)
    return perfect_numbers

perfect_numbers = find_perfect_numbers(1000000)
print("Perfect numbers less than 1000000:", perfect_numbers)
