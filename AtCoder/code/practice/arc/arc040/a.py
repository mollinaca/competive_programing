#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
r = 0
b = 0
for _ in range(n):
    s = input()
    r += s.count('R')
    b += s.count('B')

if b < r:
    print ("TAKAHASHI")
elif b > r:
    print ("AOKI")
else:
    print ("DRAW")
