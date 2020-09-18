#!/usr/bin/env python3
# -*- coding: utf-8 -*-
w,h,x,y,r = map(int,input().split())
print ("Yes") if 0 <= x-r and 0 <= y-r and x+r <= w and y+r <= h else print ("No")