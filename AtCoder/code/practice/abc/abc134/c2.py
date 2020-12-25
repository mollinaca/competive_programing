#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

A2 = sorted(A)
max1 = A2[-1]
max2 = A2[-2]

for a in A:
    if a == max1:
        print (max2)
    else:
        print (max1)
