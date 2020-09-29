#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = list(input())
a,b,c,d = map(int,input().split())
ans = ''
for i,x in enumerate(s):
    if i == a or i == b or i == c or i == d:
        ans += '"'
    ans += x

if d == len(s):
    ans += '"'

print (ans)
