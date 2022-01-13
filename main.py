def input1():
    return int(input()), int(input())


def cube(w, e):
    q = []
    for i in range(w):
        q.append([e] * w)
    return q


def sum_(a, b):
    return a + b



def factorial(number: int) -> int:
    if not number:
        return 1
    else:
        return factorial(number - 1) * number

def average(a, b):
    return (a + b) / 2





if __name__ == '__main__':
    pass
