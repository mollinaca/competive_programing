#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,K = map(int,input().split())
A = list(map(int,input().split()))
S = [0]
for i,a in enumerate(A):
    S.append(S[i]+a)

print (sum(S[-K::])-sum(S[0:K]))
