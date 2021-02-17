#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))
X = 0
for i in range(1,n):
    X += A[i]-A[i-1]

print (X/(n-1))
