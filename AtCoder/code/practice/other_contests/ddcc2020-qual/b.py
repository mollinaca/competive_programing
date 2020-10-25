#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))

l2 = []
l3 = []
for i in range(n):
    if i == 0:
        l2.append(0)
        l3.append(sum(l))
    else:
        l2.append(l2[i-1]+l[i-1])
        l3.append(l3[i-1]-l[i-1])

ans = float('inf')
for i in range(n):
    if abs(l2[i]-l3[i]) < ans:
        ans = abs(l2[i]-l3[i])

print (ans)
