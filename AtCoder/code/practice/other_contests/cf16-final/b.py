#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

if n == 1:
    print (1)
    exit ()

if n == 2:
    print (2)
    exit ()

a = 0
for i in range(1,n):
    a += i
    if n < a:
        x = a-n
        for j in range(1,i+1):
            if not j == x:
                print (j)
        exit ()

    if n == a:
        for j in range(1,i+1):
            print (j)
        exit ()
