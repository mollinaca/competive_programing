#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://twitter.com/e869120/status/1376665578513989633
N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))
A2 = []
for i,a in enumerate(A):
    if i == 0:
        A2.append(a)
    else:
        A2.append(a-A[i-1])

print (A2)

# 思ったよりムズカシかった。。。続きはまたこんど
