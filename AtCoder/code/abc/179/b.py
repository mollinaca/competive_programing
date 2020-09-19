#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

z_count = 0
for _ in range(n):
    d1,d2 = map(int,input().split())
    if d1 == d2:
        z_count += 1
    else:
        z_count = 0

    if z_count == 3:
        print ("Yes")
        exit ()

print ('No')
