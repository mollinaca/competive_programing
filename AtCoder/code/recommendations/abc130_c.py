#!/usr/bin/env python3
# -*- coding: utf-8 -*-
w,h,x,y = map(int,input().split())
if x*2 == w and y*2 == h:
    print ((w*h)/2,1)
else:
    print ((w*h)/2,0)