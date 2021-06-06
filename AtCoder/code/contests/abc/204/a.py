#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(map(int,input().split()))

if l[0] == l[1]:
    print (l[0])
else:
    if 0 not in l:
        print (0)
    elif 1 not in l:
        print (1)
    else:
        print (2)
