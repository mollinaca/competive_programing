#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M,T = map(int,input().split())
t = 0
n = N
for _ in range(M):
    a,b = map(int,input().split())
    n -= (a-t)
    t = a
    
    if n <= 0:
        print ("No")
        exit ()
    
    n = min(N,n+(b-a))
    t = b

n -= (T-t)
if n <= 0:
    print ("No")
else:
    print ("Yes")
