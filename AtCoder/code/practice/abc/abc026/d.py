#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A,B,C = map(int,input().split())
low = 0
up = 100
t = (low+up)/2

import math
while low < up - 10**(-10):
    t = (low+up)/2
    x = A*t + B*math.sin(C*t*math.pi)
    if x == 100:
        break
    elif x > 100:
        up = t
    else:
        low = t

print (t)
