#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
if n == n & -n:
    print(-1,-1,-1)
else:
    print(n, n & -n, n ^ (n & -n))
