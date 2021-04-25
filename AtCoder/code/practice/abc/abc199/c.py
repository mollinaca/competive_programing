#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
N = int(input())
S = list(input())
Q = int(input())
t = False # T = 2 がきたら反転する

   
for _ in range(Q):
    T,A,B = map(int,input().split())
    if T == 1:
        if t: # 反転フラグON
            if A <= N:
                A = A+N
            else:
                A = A-N
            if B <= N:
                B = B+N
            else:
                B = B-N

            tmp = S[A-1]
            S[A-1] = S[B-1]
            S[B-1] = tmp

        else: # t == False
            tmp = S[A-1]
            S[A-1] = S[B-1]
            S[B-1] = tmp
    else: # T == 2:
        if t: 
            t = False
        else:
            t = True

if t:
    s = []
    s.append(S[N::])
    s.append(S[0:N])
    S = list(itertools.chain.from_iterable(s))

print(''.join(map(str,S)))
