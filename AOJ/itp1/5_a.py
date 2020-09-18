#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        exit ()
    for _ in range(h):
        for _ in range(w):
            print ("#",end="")
        print ()
    print ()
