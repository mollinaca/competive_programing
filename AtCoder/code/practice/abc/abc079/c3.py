#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S = list(input())
n = len(S)-1

for i in range(2**n):
    l = ['+']*n
    for j in range(n):
        if ((i>>j)&1):
            l[n-1-j] = '-'

    X = ''
    for i in range(n):
        X += S[i]+l[i]
    X += S[-1]

    if eval(X) == 7:
        print (X+'=7')
        exit ()
