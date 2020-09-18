#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
p = True
for i in range(1,n+1):
    p = True
    if i%2 == 0:
        print ("a",end="")
        p = False
    if i%3 == 0:
        print ("b",end="")
        p = False
    if i%4 == 0:
        print ("c",end="")
        p = False
    if i%5 == 0:
        print ("d",end="")
        p = False
    if i%6 == 0:
        print ("e",end="")
        p = False
    if p:
        print (i,end="")
    print ()