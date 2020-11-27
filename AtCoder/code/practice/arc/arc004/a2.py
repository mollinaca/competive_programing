#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = []
for _ in range(n):
    n,m = map(int,input().split())
    l.append((n,m))

ans = 0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        t = ((l[i][0] - l[j][0])**2 + (l[i][1] - l[j][1])**2)**(1/2)
        if ans < t:
            ans = t

print (ans)
