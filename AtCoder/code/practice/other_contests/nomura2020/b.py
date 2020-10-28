#!/usr/bin/env python3
# -*- coding: utf-8 -*-
T = input()
ans = ''
for i,t in enumerate(T):
    if t == '?':
        ans += 'D'
    else:
        ans += t

print (ans)
