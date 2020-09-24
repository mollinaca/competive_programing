#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter
n,m = map(int,input().split())
l = list(map(int,input().split()))
c = Counter(l)
for i in range(1,m+1):
    print (i,c[i])
