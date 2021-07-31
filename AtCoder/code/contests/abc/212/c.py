#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bisect
N,M = map(int,input().split())
A = sorted(list(set(list(map(int,input().split())))))
B = sorted(list(set(list(map(int,input().split())))))
lenA = len(A)
lenB = len(B)

ans = float('inf')
if lenA <= lenB:
    for a in A:
        i = bisect.bisect_right(B,a)
        if i == 0:
            ans = min(ans, abs(a-B[i]))
        elif i == lenB:
            ans = min(ans, abs(a-B[i-1]))
        else:
            ans = min(ans, abs(a-B[i]), abs(a-B[i-1]))

elif lenB < lenA:
    for b in B:
        i = bisect.bisect_right(A,b)
        if i == 0:
            ans = min(ans, abs(b-A[i]))
        elif i == lenA:
            ans = min(ans, abs(b-A[i-1]))
        else:
            ans = min(ans, abs(b-A[i]), abs(b-A[i-1]))

print (ans)
