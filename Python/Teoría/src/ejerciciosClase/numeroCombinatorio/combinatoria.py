def factorial(n):
    r = 0
    if n == 0:
        r = 1
    else:
        r = n * factorial(n - 1)
    return r