#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = [1,1]
for i in range(n-1):
    l += [l[i]+l[i+1]]
print(l[-1])
