#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
T = int(input())
L,X,Y = map(int,input().split())
Q = int(input())
p = (0,0,0)
for _ in range(Q):
    E = int(input())
    p = (0, -1*((L/2)*math.sin(360*(E/T))), (L/2)-((L/2)*math.cos(360*(E/T))))
    print (p)
    A = math.sqrt(X**2 + (p[1]-Y)**2)
    B = p[2]
    print (math.atan2(A,B))
