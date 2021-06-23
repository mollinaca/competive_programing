#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k = int(input())
x = '7'
for i in range(1,10**4):
    if int(x*i)%k == 0:
        print (i)
        exit ()

print (-1)
