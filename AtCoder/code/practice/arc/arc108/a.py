#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s,p = map(int,input().split())
for i in range((10**6)+1):
    if i*(s-i) == p:
        print ('Yes')
        exit ()
else:
    print ('No')
