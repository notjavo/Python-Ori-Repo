def fibonacci(limit):
    a, b = 0, 1
    total_sum = 0

    while b < limit:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b
    return total_sum

limit = 4000000
result = fibonacci(limit)

print(f"The sum of all even Fibonacci numbers below {limit} is {result}")


