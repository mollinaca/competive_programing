#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
sA = sum(A)
X = int(input())

# 累積和
W = []
for i,a in enumerate(A):
    if i == 0:
        W.append(a)   
    else:
        W.append(W[i-1]+a)

X2 = X//sA
X3 = X-(X2*sA)

import bisect
print (N*X2+bisect.bisect_right(W,X3)+1)
