#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))

ans = -1
ans_g = 0
for i in range(2,1001):
    g = 0
    for x in l:
        if x%i == 0:
            g += 1

    if ans_g < g:
        ans = i
        ans_g = g
    
print (ans)
