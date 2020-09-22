#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))
total_A = [0]
for i,v in enumerate(A):
    total_A.append(total_A[i]+v)

for i in range(1,n+1):
    ans = 0
    for j in range(n+1-i):
        ans = max(total_A[j+i]-total_A[j],ans)
    
    print (ans)
