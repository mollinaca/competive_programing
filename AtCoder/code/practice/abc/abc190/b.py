#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,S,D = map(int,input().split())
for _ in range(N):
    X,Y = map(int,input().split())

    if X < S and D < Y:
        print ('Yes')
        exit ()
print ('No')
