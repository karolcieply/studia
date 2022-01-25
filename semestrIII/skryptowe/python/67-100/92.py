from math import *


def silnia(n):
    return n * silnia(n - 1) if n > 1 else 1


def a():
    alfa = radians(int(input("alfa: ")))
    beta = radians(int(input("beta: ")))
    print(sin(alfa) + sin(beta))
    print(2 * sin(1 / 2 * (alfa + beta)) * cos(1 / 2 * (alfa - beta)))


def b():
    x = int(input("x: "))
    n = int(input("n: "))
    result = 1 + ((n * x) / silnia(1))
    for i in range(2, 10):
        result += (n * (n - i) * (x ** i)) / silnia(i)
    print((1 + x) ** n)
    print(result)


def c():
    a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))
    print((-b + sqrt(b * b - 4 * a * c)) / 2 * a)


def d():
    result = 1
    x = int(input("x: "))
    for i in range(1, 20):
        result = result + (x ** i) / silnia(i)
    print(result)
    print(exp(x))
