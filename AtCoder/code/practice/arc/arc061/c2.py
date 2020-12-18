#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S = input()
ans = 0

n = len(S)-1
for i in range(2**n):
    l = [0]*n
    for j in range(n):
        if ((i>>j)&1):
            l[n-1-j] = 1

    X = ''
    for i in range(n):
        X += S[i]
        if l[i] == 1:
            X += '+'
    X += S[-1]
    ans += eval(X)

print (ans)
