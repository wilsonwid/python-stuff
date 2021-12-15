def fibonacci_iter(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b



string = str(fibonacci_iter(100000))
print(len(string))
print(fibonacci_iter(4))
