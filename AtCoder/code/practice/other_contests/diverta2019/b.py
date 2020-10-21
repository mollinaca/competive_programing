#!/usr/bin/env python3
# -*- coding: utf-8 -*-
R,G,B,N = map(int,input().split())
ans = 0

for r in range((N//R)+1):
    for g in range((N-(R*r)//G)+1):
        if (N-(r*R)-(g*G)) < 0:
            break
        if (N-(r*R)-(g*G))%B == 0:
            ans += 1

print (ans)
