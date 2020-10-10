#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

def digsum(a:int) -> int:
    res = 0
    while a>0:
        res += a%10
        a //= 10
    return res

print (10) if n%10 == 0 else print(digsum(n))
