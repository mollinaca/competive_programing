#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter
def factorization(n):
    d = Counter()
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            d[i] += 1
        else:
            i += 1
 
    d[n] += 1
    return d

n, p = map(int,input().split())

factors = factorization(p)
ans = 1
if n == 1:
    ans = p
else:
    for k,v in factors.items():
        a = v//n
        ans *= k**a

print (ans)
