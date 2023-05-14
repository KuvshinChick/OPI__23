#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
from threading import Thread

eps = 10 ** (-7)


def check_sum(x):
    result = (math.e ** x - math.e ** (-x)) / 2
    print(f"The check is: {result}")


def inf_sum(x):
    a = (x ** 2) / 20
    S = a
    n = 1

    while math.fabs(a) > eps:
        a *= (x ** 2) / ((2 * n + 2) * (2 * n + 3))
        S += a
        n += 1

    print(f"The sum is: {S}")


if __name__ == '__main__':
    x = 2
    thread1 = Thread(target=check_sum(x))
    thread2 = Thread(target=inf_sum(x))
    thread1.start()
    thread2.start()
