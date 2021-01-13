#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

t = 0
for a,b in zip(A,B):
    t += a*b

print ("Yes") if t == 0 else print ("No")
