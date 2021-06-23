#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
X = 0
x = []
for _ in range(N):
    A,B = map(int,input().split())
    X -= A
    x.append((2*A)+B)
x.sort()

ans = 0
while X <= 0:
    X += x.pop()
    ans += 1
print (ans)
