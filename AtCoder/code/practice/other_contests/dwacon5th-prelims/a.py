#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int,input().split()))
avg = sum(a)/len(a)
ans = 0
tmp = float('inf')

for i,v in enumerate(a):
    if abs(avg-v) < tmp:
        tmp = abs(avg-v)
        ans = i

print (ans)
