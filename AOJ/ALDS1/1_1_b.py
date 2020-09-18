#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x,y = map(int,input().split())

def divs(n:int):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    return divs

print (max(set(divs(x))&set(divs(y))))
