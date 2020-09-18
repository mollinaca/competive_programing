#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
d = {}

for i in range(n):
    d[i]=list(map(str,input().split()))

for mark in ['S','H','C','D']:
    for i in range(1,14):
        if not [mark,str(i)] in d.values():
            pass
            print (mark,i)
