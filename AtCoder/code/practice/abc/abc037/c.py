#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,K = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
for i in range(len(A)-(K-1)):
    ans += sum(A[i:i+K])

print (ans)
