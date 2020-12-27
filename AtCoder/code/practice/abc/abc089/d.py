#!/usr/bin/env python3
# -*- coding: utf-8 -*-
H,W,D = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
Q = int(input())

def search (p:int):
    for y,line in enumerate(A):
        if p in line:
            for x,l in enumerate(line):
                if l == p:
                    return (y+1,x+1)

LR = {}
for i in range(1,Q+1):
    ans = 0
    L,R = map(int,input().split())
    LR[i] = [L,R]

    f = True
    for t in range(L,R+1,D):
        if f:
            px,py = search(t)
            f = False
        else:
            x,y = search(t)
            ans += abs(x-px) + abs(y-py)
            px,py = x,y


    print (ans)
