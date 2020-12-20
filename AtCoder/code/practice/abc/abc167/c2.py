#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M,X = map(int,input().split())
C = []
A = {}
for i in range(1,N+1):
    l = list(map(int,input().split()))
    C.append(l[0])
    A[i] = l[1::]

ans = float('inf')
for i in range(2**N):
    B = [0]*N
    for j in range(N):
        if ((i>>j)&1):
            B[N-1-j] = 1

    # 条件が成立するか確認
    rikaido = [0]*M
    cost = 0
    rikai = False
    for j,b in enumerate(B):
        if b == 0: # j番目の参考書を買ってない
            pass
        else: # 買った
            cost += C[j]
            for k,a in enumerate(A[j+1]):
                rikaido[k] += a

    for r in rikaido:
        if r < X:
            break
    else:
        if cost < ans:
            ans = cost

if ans == float('inf'):
    print (-1)
else:
    print (ans)
