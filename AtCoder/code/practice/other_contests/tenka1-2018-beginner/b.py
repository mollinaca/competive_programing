#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,k = map(int,input().split())

for i in range(k):
    if i%2 == 0:
        # takahashi turn
        if not a%2 == 0:
            a -= 1
        b += a/2
        a /= 2

    else:
        # aoki turn
        if not b%2 == 0:
            b -= 1    
        a += b/2
        b /= 2

print (int(a), int(b))
