#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x,k,d = map(int,input().split())
x = abs(x)
if k*d <= x:
    print (abs(x-(k*d)))
else:
    k -= x//d
    x -= d*(x//d)
    if k%2 == 0:
        print (x)
    else:
        print (abs(x-d))
