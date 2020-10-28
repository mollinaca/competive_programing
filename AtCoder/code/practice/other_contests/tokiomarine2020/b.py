#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())

if V <= W:
    print ("NO")
    exit ()

if abs(A-B)/(V-W) <= T:
    print ("YES")
else:
    print ("NO")
