#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))
ans = 0
prev_h = 0
for i,h in enumerate(A):
    if i == 0:
        prev_h = h
    else:
        if h < prev_h:
            ans += prev_h - h
        else:
            prev_h = h

print (ans)
