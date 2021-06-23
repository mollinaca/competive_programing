#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,X = map(int,input().split())
A = 0
for i in range(1,N+1):
    V,P = map(int,input().split())
    A += V*P
    if X*100 < A:
        print (i)
        exit ()
print (-1)
