#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        exit ()
    for i in range(h):
        if i%2 == 0:
            for j in range(w):
                print ("#",end="") if j%2 == 0 else print (".",end="")
        else:
            for j in range(w):
                print (".",end="") if j%2 == 0 else print ("#",end="")
        print ()
    print ()
