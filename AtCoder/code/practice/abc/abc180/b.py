#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(abs,map(int,input().split())))
m = 0
u = 0
c = max(l)

for i in l:
    m += i
    u += i**2

print (m)
print (u**(1/2))
print (c)
