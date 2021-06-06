#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))

ans = 0
for a in A:
    if a <= 10:
        pass
    else:
        ans += a-10
print (ans)
