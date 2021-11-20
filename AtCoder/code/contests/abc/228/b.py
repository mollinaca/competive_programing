#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,X = map(int,input().split())
A = list(map(int,input().split()))
A2 = [False]*N

ans = 0
x = X-1
while True:
    if A2[x] is False:
        ans += 1
        A2[x] = True
        x = A[x]-1
    else:
        print (ans)
        exit ()
