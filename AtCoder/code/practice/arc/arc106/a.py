#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

for i in range(1,100):
    for j in range(1,100):
        if 3**i + 5**j == n:
            print (i,j)
            exit ()

print (-1)
