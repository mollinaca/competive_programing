#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = input()
b = input()
c = input()

ans = 0
for x,y,z in zip(a,b,c):
    ans += len(set([x,y,z]))-1
print (ans)
