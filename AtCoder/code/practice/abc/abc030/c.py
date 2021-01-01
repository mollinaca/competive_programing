#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M = map(int,input().split())
X,Y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

import bisect

ans = 0
ai = 0
bi = 0
time = A[ai]
while True:
    time = A[ai] + X
    if B[-1] < time:
        break
    else:
        bi = bisect.bisect_left(B, time)
        time = B[bi] + Y
        ans += 1

        if A[-1] < time:
            break

        ai = bisect.bisect_left(A, time)

print (ans)
