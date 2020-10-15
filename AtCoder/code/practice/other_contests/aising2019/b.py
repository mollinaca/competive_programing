#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
p1 = []
p2 = []
p3 = []
for i in p:
    if i <= a:
        p1.append(i)
    elif a+1 <= i <= b:
        p2.append(i)
    else:
        p3.append(i)

print (min(len(p1),len(p2),len(p3)))
