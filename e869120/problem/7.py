#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bisect
N = int(input())
A = sorted(list(map(int,input().split())))
Q = int(input())
for _ in range(Q):
    B = int(input())
    b = bisect.bisect_left(A,B)
    if b == 0:
        print (A[b]-B)
    elif b == N:
        print (B-A[b-1])
    else:
        print (min(abs(A[b-1]-B),abs(A[b]-B)))
