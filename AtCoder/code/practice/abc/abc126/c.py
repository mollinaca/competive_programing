#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int,input().split())
ans = 0

for i in range(1,n+1):
    tmp = 1
    now = i
    while now < k:
        now = now*2
        tmp = tmp*0.5
    ans += tmp*(1/n)
print (ans)
