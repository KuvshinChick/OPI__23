#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
from threading import Thread

eps = 10 ** (-7)


def check_sum(x):
    result = (math.e ** x - math.e ** (-x)) / 2
    print(f"The check is: {result}")


def inf_sum(x):
    summa = 1.0
    n = 1
    temp = 0
    f = 1
    while abs(summa - temp) > eps:
        temp = summa
        if n > 0:
            f *= (2 * n) * (2 * n + 1)
        summa += x ** (2 * n + 1) / f
        n += 1

    print(f"The sum is: {summa}")


if __name__ == '__main__':
    x = 2
    thread1 = Thread(target=check_sum(x))
    thread2 = Thread(target=inf_sum(x))
    thread1.start()
    thread2.start()
