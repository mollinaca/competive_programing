#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S = input()
A = 'CODEFESTIVAL2016'
ans = 0
for a,s in zip(A,S):
    if not a == s:
        ans += 1
print (ans)
