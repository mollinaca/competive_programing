#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
P = int(input())

max_x = 0
for x in range(20):
    max_x = x
    if P < math.factorial(x):
        max_x -= 1
        break

ans = 0
for x in range(max_x,0,-1):
    y = P//math.factorial(x)
    P = P - y*math.factorial(x)
    ans += y
    if P == 0:
        break

print (ans)
