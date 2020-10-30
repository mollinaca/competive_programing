#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))
ans = 0
for i,v in enumerate(l):
    if l[v-1] == i+1:
        ans += 1

print (ans//2)
