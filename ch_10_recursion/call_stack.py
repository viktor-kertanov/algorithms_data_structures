def func_three():
    print("Three")


def func_two():
    func_three()
    print("Two")


def func_one():
    func_two()
    print("One")


def func_recursive():
    print(f"Hello world!")
    func_recursive()


if __name__ == '__main__':
    # func_recursive() # for looking at call stack in debugger. don't run without a debugger
    func_one()
    print("Hello world!")