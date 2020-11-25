#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,x = map(int,input().split())
s = input()
for i in s:
    if i == 'x':
        if 0 < x:
            x -= 1
    else:
        x += 1
print (x)
