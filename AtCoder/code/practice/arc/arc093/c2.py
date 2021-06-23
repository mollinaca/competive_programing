#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,input().split()))
sA = sorted(A)
maxa = sA[-1]
maxa2 = sA[-2]
mina = sA[0]
mina2 = sA[1]

suma = 0
A2 = [0]
for i,a in enumerate(A):
    suma += A2[i-1]+abs(a-A[i-1])


if 0 <= mina:
    mina2 = mina
    mina = 0
    # 最小値は気にしなくて良い
    for a in A:
        if a == maxa:
            print (suma-((maxa-maxa2)*2))
        else:
            print (suma)
elif mina < 0 < maxa:
    mina2 = min(mina2,0)
    # 最小最大どちらも気にする
    for a in A:
        if a == maxa:
            print (suma-((maxa-maxa2)*2))
        elif a == mina:
            print (suma-((abs(mina)-abs(mina2))*2))
        else:
            print (suma)

else:
    maxa2 = maxa
    maxa = 0
    # 最大値は気にしなくて良い
    for a in A:
        if a == mina:
            print (suma-((abs(mina)-abs(mina2))*2))
        else:
            print (suma)
