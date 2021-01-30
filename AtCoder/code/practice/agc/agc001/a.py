#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = sorted(list(map(int,input().split())))
ans = 0
for i in range(0,2*n,2):
    ans += min(l[i],l[i+1])
print (ans)
