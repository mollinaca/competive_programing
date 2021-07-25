#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
l = {}
n = 0
for _ in range(N):
    n += 1
    s = input()
    if s in l:
        pass
    else:
        l[s] = 1
        print (n)
