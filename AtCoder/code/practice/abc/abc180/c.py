#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

def divs(n:int) -> list:
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    divs.sort()
    return divs

ans = divs(n)
for i in ans:
    print (i)
