#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = sorted(list(map(int,input().split())))
B = list(map(int,input().split()))
C = sorted(list(map(int,input().split())))

import bisect

ans = 0
for b in B:
    i = bisect.bisect_left(A,b)
    k = bisect.bisect_right(C,b)
    ans += i*(n-k)

print (ans)
