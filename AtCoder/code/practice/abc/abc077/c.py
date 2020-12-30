#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

import bisect

ans = 0
for a in A:
    x = bisect.bisect_right(B,a)
    for b in B[x::]:
        y = bisect.bisect_right(C,b)
        ans += len(C[y::])

print (ans)
