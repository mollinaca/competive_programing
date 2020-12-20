#!/usr/bin/env python3
# -*- coding: utf-8 -*-
red = []
blue = []
N = int(input())
for _ in range(N):
    red.append(input())
M = int(input())
for _ in range(M):
    blue.append(input())

ans = 0
for t in set(red):
    tmp = 0
    tmp += red.count(t)
    tmp -= blue.count(t)

    if ans < tmp:
        ans = tmp

print (ans)
