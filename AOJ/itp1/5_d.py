#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
for i in range(3,n+1):
    if i%3 == 0 or '3' in str(i):
        print('', i, end='')
print ()