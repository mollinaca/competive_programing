#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
for i in range(2**n):
    l = ['(']*n
    for j in range(n):
        if ((i>>j)&1):
            l[n-1-j] = ')'

    f = True
    x = 0
    for p in l:
        if p == '(':
            x += 1
        else:
            x -= 1
        if x < 0:
            f = False
            break
    
    if f and x == 0:
        print(''.join(map(str, l)))
