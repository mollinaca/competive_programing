#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S = reversed(input())
o = 0
e = 0
for i,s in enumerate(S):
    if (i+1)%2 == 1:
        o += int(s)
    else:
        e += int(s)
print (e,o)
