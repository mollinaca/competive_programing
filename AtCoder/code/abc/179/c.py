#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
n = int(input())
ans = 0
for i in range(1, n):
    ans += (math.ceil(n/i))-1

print (ans)
