#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A,B,C = map(int,input().split())
if C == 0:
    if A<=B:
        ans = 'Aoki'
    else:
        ans = 'Takahashi'
else:
    if B<=A:
        ans = 'Takahashi'
    else:
        ans = 'Aoki'
print (ans)
