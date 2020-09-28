#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,L = map(int,input().split())
S = list(input())
tab_count = 1
crash_count = 0

for x in S:
    if x == '-':
        tab_count -= 1
    else:
        tab_count += 1
        if tab_count == L+1:
            crash_count += 1
            tab_count = 1

print (crash_count)
