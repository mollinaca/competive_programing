#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
N = int(input())
X = [i for i in range(N)]
A = list(map(int,input().split()))

ans = 0
for i,j in itertools.combinations(X,2):
    if (A[i]-A[j])%200 == 0:
        ans += 1

print (ans)
