#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = [0] + list(map(int,input().split())) + [0]
S = 0

for i in range(1,len(A)):
    S += abs(A[i]-A[i-1])

for i in range(1,len(A)-1):
    print (S + abs(A[i-1]-A[i+1]) - (abs(A[i-1]-A[i])+abs(A[i]-A[i+1])))
