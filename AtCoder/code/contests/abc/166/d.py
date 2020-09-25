#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x = int(input())

p = 0
while True:
    p += 1
    for i in range(-p,p):
        for j in range(-p,p):
            if i**5 - j**5 == x:
                print (i,j)
                exit ()
