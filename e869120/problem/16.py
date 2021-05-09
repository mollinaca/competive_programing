#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A,B,C = sorted(map(int,input().split()))
c = N//C

for z in range(c,-1,-1):
    b = (N-z*C)//B
    for y in range(b,-1,-1):
        if N < B*y + C*z:
            break

        if (N-(y*B+z*C))%A == 0:
            x = (N-(y*B+z*C))//A
            print (x+y+z)
            exit ()
