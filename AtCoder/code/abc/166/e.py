#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))
c = 0
for i in range(n-1):
    for j in range(i+1,n):
        if A[i]+A[j] == j-i:
            c += 1
print (c)
