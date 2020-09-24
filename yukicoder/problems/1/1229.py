#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
ans = 0
i = j = k = 0

for i in range((n//5)+1):
    for j in range(i+1):
        for k in range((n//3)+1):
            if 5*i + 2*j + 3*k == n:
                ans += 1
                continue

print (ans)