#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M = map(int,input().split())
state = {}
born = {}

import bisect
for i in range(1,M+1):
    p,y = map(int,input().split())
    born[i] = [p,y]
    if p in state:
        bisect.insort_left(state[p],y)
    else:
        state[p] = [y]

for k,v in born.items():
    i = bisect.bisect_left(state[v[0]],v[1])
    ans = str(v[0]).zfill(6) + str(i+1).zfill(6)
    print (ans)
