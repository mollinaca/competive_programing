#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = sorted(list(map(int,input().split())))

def divs(n:int) -> set:
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    divs.sort()
    return set(divs)

d = {}
for i in l:
    d[i] = (divs(i))

ans = {}
for k,v in d.items():
    if k == l[0]:
        ans = v
    else:
        ans = ans&v

for i in sorted(ans):
    print (i)
