#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

ans = 0
for _ in range(n):
    n,m = map(int,input().split())
    ans += m-n+1

print (ans)
