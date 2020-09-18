#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = 0
B = 0
for _ in range(n):
    x,y = input().split()
    if x > y:
        A += 3
    elif y > x:
        B += 3
    else:
        A += 1
        B += 1
print (A,B)
