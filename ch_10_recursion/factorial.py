def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


if __name__ == '__main__':
    n = 5
    factorial_n = factorial(n)
    print(f"{n}! = {factorial_n}")
    print('Hello world!')