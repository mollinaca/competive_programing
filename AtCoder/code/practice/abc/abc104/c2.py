#!/usr/bin/env python3
# -*- coding: utf-8 -*-
D,G = map(int,input().split())
P = {}
C = {}
X = {} # 問 i を全部解いたときの得点（コンプリートボーナス込）
Y = {} # 問 i を1問残して解いたときの得点

for i in range(1,D+1):
    n,m = map(int,input().split())
    P[i] = n
    C[i] = m
    X[i] = (100*i*n)+m
    Y[i] = 100*i*(n-1)

def f1 (l:list) -> tuple:
    # bit から得られる得点と解いた問題数を返す
    r = 0
    s = 0
    for a,b in enumerate(l):
        if b == 1:
            r += X[a+1]
            s += P[a+1]

    return r,s

def f2 (l:list) -> int:
    # bit から、0がたってる最も高いbitの index+1 を返す
    for a,b in enumerate(reversed(l)):
        if b == 0:
            return len(l)-a

ans = float('inf')
for i in range(2**D):
    bit = [0]*D
    for j in range(D):
        if ((i>>j)&1):
            bit[D-1-j] = 1

#    print (bit) # 0 の問題は解いてない、1の問題は解いた
    score = f1(bit)

    if bit.count(0) == 0:
        # 全問解いたパターン
        if G <= score[0]: # 問題の制約より絶対Trueになる
            if score[1] < ans:
                ans = score[1]
    else:
        # 1問以上残ってるパターン
        if G <= score[0]:
            if score[1] < ans:
                ans = score[1]
        else:
            # 最も高いbitをあと数問解いたらGに達するかどうか
            bi = f2(bit)
            if G <= score[0] + Y[bi]:
                # 達する
                # 何問解けばよいか？
                left_score = G - score[0]
                left_p = -(-left_score//(100*bi))
                if score[1] + left_p < ans:
                    ans = score[1] + left_p

print (ans)
