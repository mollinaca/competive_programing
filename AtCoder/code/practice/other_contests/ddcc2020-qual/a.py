#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x,y = map(int,input().split())
ans = 0

if x == 1:
    ans += 300000
elif x == 2:
    ans += 200000
elif x == 3:
    ans += 100000
else:
    pass

if y == 1:
    ans += 300000
elif y == 2:
    ans += 200000
elif y == 3:
    ans += 100000
else:
    pass

if x == y == 1:
    ans += 400000

print (ans)
