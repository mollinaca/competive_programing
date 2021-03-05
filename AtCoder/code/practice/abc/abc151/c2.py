#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M = map(int,input().split())

ac = 0
wa = 0
d_ac = {}
d_wa = {}
for _ in range(M):
    p,s = input().split()
    p = int(p)

    if p not in d_ac:
        d_ac[p] = False
        d_wa[p] = 0

    if s == "WA":
        if d_ac[p]:
            pass
        else:
            d_wa[p] += 1
    else: # s == "AC"
        if d_ac[p]:
            pass
        else:
            d_ac[p] = True
            ac += 1
            wa += d_wa[p]

print (ac,wa)
