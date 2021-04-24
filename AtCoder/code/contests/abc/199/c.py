#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools

N = int(input())
S = list(input())
Q = int(input())
for _ in range(Q):
    T,A,B = map(int,input().split())
    s = []
    if T == 1:
        if A == 1 and B == 2*N:
            s.append(S[B-1])
            s.append(S[A:B-1])
            s.append(S[A-1])
            S = list(itertools.chain.from_iterable(s))
        elif A == 1:
            s.append(S[B-1])
            s.append(S[1:B-1])
            s.append(S[A-1])
            s.append(S[B::])
            S = list(itertools.chain.from_iterable(s))
        elif B == 2*N:
            s.append(S[0:A-1])
            s.append(S[B-1])
            s.append(S[A:B-1])
            s.append(S[A-1])
            S = list(itertools.chain.from_iterable(s))
        else:
            s.append(S[0:A-1])
            s.append(S[B-1])
            s.append(S[A:B-1])
            s.append(S[A-1])
            s.append(S[B::])
            S = list(itertools.chain.from_iterable(s))
    else: # T == 2:
        s.append(S[N::])
        s.append(S[0:N])
        S = list(itertools.chain.from_iterable(s))

print(''.join(map(str, S)))
