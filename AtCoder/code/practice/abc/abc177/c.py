#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
n = int(input())
A = list(map(int,input().split()))
A_total = sum(A)
ans = 0
for i in A:
    A_total -= i
    ans += i*A_total

print (ans%((10**9)+7))
