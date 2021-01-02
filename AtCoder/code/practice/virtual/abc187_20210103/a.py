#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A,B = input().split()
sumA = 0
sumB = 0
for a,b in zip(A,B):
    sumA += int(a)
    sumB += int(b)

print (sumA) if sumB < sumA else print(sumB)
