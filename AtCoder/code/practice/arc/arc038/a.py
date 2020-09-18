#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = sorted(list(map(int,input().split())),reverse=True)
print (sum(l[0::2]))
