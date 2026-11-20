def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def greet():
    return "Welcome to Calculator v2 - now with Multiply"


if __name__ == "__main__":
    print(greet())
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 3 =", multiply(4, 3))
