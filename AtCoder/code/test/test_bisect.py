#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))

A = sorted(l)
print (A)

import bisect
print (bisect.bisect_left(A,n))
print (bisect.bisect_right(A,n))
