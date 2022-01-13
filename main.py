def input1():
    return int(input()), int(input())


def factorial(number: int) -> int:
    if not number:
        return 1
    else:
        return factorial(number - 1) * number


if __name__ == '__main__':
    pass
