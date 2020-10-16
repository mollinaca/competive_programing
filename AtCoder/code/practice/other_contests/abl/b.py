#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c,d = map(int,input().split())
if a < c:
    if c <= b:
        print ('Yes')
        exit ()
elif c < a:
    if a <= d:
        print ('Yes')
        exit ()
else:
    print ('Yes')
    exit ()

print ('No')
