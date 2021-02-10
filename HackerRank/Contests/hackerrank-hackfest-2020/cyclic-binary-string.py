#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://www.hackerrank.com/contests/hackerrank-hackfest-2020/challenges/cyclic-binary-string/problem
S = input()
S2 = S+S
N = len(S)

ans = 0
m = 0
for i in range(N):
    X = int(S2[i:i+N])
    if len(str(X)) < m:
        continue
    m = len(str(X))

    t = 0
    while True:
        if X%2 == 0:
            X = X//2
            t += 1
        else:
            break
    
    ans = max(ans,t)

print (ans)
