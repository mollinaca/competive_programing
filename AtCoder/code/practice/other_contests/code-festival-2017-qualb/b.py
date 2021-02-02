#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

for t in T:
    if t in D:
        D.remove(t)
    else:
        print ("NO")
        exit ()
print ("YES")
