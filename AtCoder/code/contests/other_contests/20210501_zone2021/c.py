#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
N = int(input())
x = [i for i in range(N)]
A,B,C,D,E = [],[],[],[],[]
for _ in range(N):
    a,b,c,d,e = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    E.append(e)

ans = 0
for v in itertools.combinations(x,3):
    aa = 0
    for i in v:
        aa = max(aa,A[i])
    bb = 0
    for i in v:
        bb = max(bb,B[i])
    cc = 0
    for i in v:
        cc = max(cc,C[i])
    dd = 0
    for i in v:
        dd = max(dd,D[i])
    ee = 0
    for i in v:
        ee = max(ee,E[i])
    a = min(aa,bb,cc,dd,ee)
    ans = max(ans,a)

print (ans)
