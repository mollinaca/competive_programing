#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = []
b = []
c = []
for _ in range(n):
    l = sorted(list(map(int,input().split())))
    a.append(l[0])
    b.append(l[1])
    c.append(l[2])

print (max(a)*max(b)*max(c))
