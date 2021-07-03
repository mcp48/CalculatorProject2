def addition(a, b):
    return int(a) + int(b)


def subtraction(a, b):
    return int(a) - int(b)


def multiplication(a, b):
    return int(a) * int(b)


def division(a, b):
    round_result = a / b
    return round(round_result, 8)


def square(a):
    return a ** 2


def squareRoot(a):
    round_root = a ** 0.5
    return round(round_root, 8)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareRoot(self, a):
        self.result = squareRoot(a)
        return self.result

