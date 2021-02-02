#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))
D2 = {}
T2 = {}
for d in D:
    if d not in D2:
        D2[d] = 1
    else:
        D2[d] += 1

for t in T:
    if t not in T2:
        T2[t] = 1
    else:
        T2[t] += 1

for tk,tv in T2.items():
    if tk not in D2:
        print ("NO")
        exit ()
    elif D2[tk] < T2[tk]:
        print ("NO")
        exit ()
    else:
        pass
print ("YES")
