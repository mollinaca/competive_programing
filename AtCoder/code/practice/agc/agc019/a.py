#!/usr/bin/env python3
# -*- coding: utf-8 -*-
q,h,s,d = map(int,input().split())
n = int(input())
if n%2 == 0:
    print(min(q*8, h*4,s*2,d)*(n//2))
else:
    print ((n//2)*(min(8*q,4*h,2*s,d)) + min((4*q,2*h,s)))
