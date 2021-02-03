#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
setA = set(A)

def c (L:list,x:int) -> int:
    ret = 0
    t = 0
    for i in L:
        if x <= i:
            t += 1
        else:
            ret = max(t,ret)
            t = 0
    else:
        ret = max(t,ret)

    return ret

ans = 0
for a in setA:
    t = a*c(A,a)
    if ans < t:
        ans = t
print (ans)
