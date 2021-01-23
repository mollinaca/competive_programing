#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))

X = [0]
X2 = [0]
for i in range(1,N+1):
    X.append(X[i-1] + A[i-1])
    X2.append(X2[i-1]+X[i])

print (max(X)+max(X2))
