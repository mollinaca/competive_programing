#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(input().split())
ans = []
for s in l:
    if s == 'Left':
        ans.append('<')
    elif s == 'Right':
        ans.append('>')
    else:
        ans.append('A')
print(' '.join(map(str, ans)))
