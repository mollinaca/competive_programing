#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
ans = 10**18
for _ in range(N):
    A,P,X = map(int,input().split())
    if 0 < -1*A + (X-0.5):
        ans = min(ans,P)

print (-1) if ans == 10**18 else print (ans)
