#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,x = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
bx = bin(x)[2:].zfill(n)
for i in range(len(bx)):
#    print (bx[n-1-i],a[i])
    ans += int(bx[n-1-i])*a[i]
print (ans)
