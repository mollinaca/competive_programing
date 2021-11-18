#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

c = 0
for a,b in zip(A,B):
    c += abs(a-b)

if c <= K:
    if abs(c-K)%2 == 0:
        print ("Yes")
        exit ()

print ("No")
