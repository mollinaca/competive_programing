#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x,y = map(int,input().split())
k = int(input())

if k <= y:
    print (x+k)
elif y < k:
    print (y+x-(k-y))
