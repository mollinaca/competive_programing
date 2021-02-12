#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    s = input()

    cu = s.count('U')
    cd = s.count('D')
    cr = s.count('R')
    cl = s.count('L')

    if x < 0:
        if cl < abs(x):
            print ('NO')
            continue
    else:
        if cr < x:
            print ('NO')
            continue
    
    if y < 0:
        if cd < abs(y):
            print ('NO')
            continue
    else:
        if cu < y:
            print ('NO')
            continue

    print ('YES')
