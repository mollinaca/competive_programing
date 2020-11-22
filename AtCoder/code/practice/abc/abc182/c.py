#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(map(int,input()))
l2 = []
for i in l:
    l2.append(i%3)

x = sum(l2)%3
if x == 0:
    print (0)
    exit ()

if x == 1:
    if x in l2 and 2 <= len(l2):
        print (1)
    elif 2 <= l2.count(2) and 2 < len(l2):
        print (2)
    else:
        print (-1)
else: # x == 2
    if x in l2 and 2 <= len(l2):
        print (1)
    elif 2 <= l2.count(1) and 2 < len(l2):
        print (2)
    else:
        print (-1)
