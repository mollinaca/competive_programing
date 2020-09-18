#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        exit ()
    else:
        print (x,y) if x <= y else print (y,x)