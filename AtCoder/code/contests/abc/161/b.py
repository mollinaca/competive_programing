#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,m = map(int,input().split())
a = sorted(list(map(int,input().split())),reverse=True)
print ("Yes") if a[m-1] >= sum(a)/(4*m) else print ("No")
