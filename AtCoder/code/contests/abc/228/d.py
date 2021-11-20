#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = 1048576
A = [-1]*N
Q = int(input())

for _ in range(Q):
    t,x = map(int,input().split())
    
    if t == 1:
        h = x
        h = h%N
        while A[h] != -1:
            h += 1
            h = h%N
        A[h] = x

    else: # t == 2
        print (A[x%N])
