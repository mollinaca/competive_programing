#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
S = string.ascii_uppercase
H,W = map(int,input().split())
for i in range(1,H+1):
    l = list(input().split())
    if "snuke" in l:
        print (S[l.index("snuke")]+str(i))
        exit ()
