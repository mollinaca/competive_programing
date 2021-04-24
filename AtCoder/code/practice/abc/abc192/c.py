#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,K = map(int,input().split())

def g1(x:int):
    x = sorted(str(x),reverse=True)
    r = ''
    for y in x:
        r += y

    return int(r)


def g2(x:int):
    x = sorted(str(x))
    r = ''
    for y in x:
        if y == '0':
            pass
        else:
            r += y
    if not r:
        r = '0'

    return int(r)

def f (n):
    return g1(n)-g2(n)

for _ in range(K):
    N = f(N)
print (N)
