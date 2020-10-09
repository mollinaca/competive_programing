#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c,k = map(int,input().split())
if k%2 == 0:
    ans = a-b
else:
    ans = b-a
print ("unfair") if 10**18 < abs(ans) else print (ans)
