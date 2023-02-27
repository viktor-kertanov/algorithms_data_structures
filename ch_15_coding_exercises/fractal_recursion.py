def fractal(num):
    if num==1:
        return 1
    print(f"Function fractal, num == {num}")
    return num*fractal(num-1)


if __name__ == "__main__":
    a = fractal(4)
    print(a)
    print('Hello world!')