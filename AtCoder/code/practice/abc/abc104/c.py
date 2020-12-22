#!/usr/bin/env python3
# -*- coding: utf-8 -*-
D,G = map(int,input().split())
P = {}
C = {}
X = {} # 各問題を全問正解した場合に得られる得点
T = {} # 各問題を全問正解せず1問だけ残して残りすべて正解した場合に得られる得点

def f1 (l:list) -> tuple:
    # 与えられたbitで得られる合計の得点と正解した問題数を返す
    r = 0
    p = 0
    for a,b in enumerate(l):
        if b == 1:
            r += X[a+1]
            p += P[a+1]
    return r,p

def f2 (l:list):# -> int:
    # 与えられたbitの最も高い0のindexを返す
    # 0 が存在しない bit は入力されない
    for a,b in (enumerate(reversed(l))):
        if b == 0:
            return (len(l)-a)

for i in range(1,D+1):
    n,m = map(int,input().split())
    P[i] = n
    C[i] = m
    X[i] = n*i*100 + m
    T[i] = 100*(n-1)

print (D,G)
print (P,C)
print ("X:",X,"T:",T)

ans = float('inf')
for i in range(2**D):
    tmp = 0
    bit = [0]*D
    for j in range(D):
        if ((i>>j)&1):
            bit[D-1-j] = 1

    # 処理
    # print (bit)
    if not bit.count(0) == 0:
        # 全問正解しないパターン
        score = f1(bit)
        index = f2(bit)
        tmp = score[1]
        print (bit, score,index) # score[0] -> 獲得得点、 score[1] -> 解いた問題数

        if G <= score[0]: # この時点でGをクリア
            if tmp < ans:
                print ("ans(1) ->",tmp,i,bit,index,score)
                ans = tmp
        else:
            # index の点数を合計してGを超えるかどうか
            if G <= score[0] + T[index]:
                # 超えるので、「全問正解が1種類以上+中途半端に1種類を解く」で条件をクリアする
                # 必要な点数分だけの問題数を tmp に追加する
                tmp += -(-(G - score[0])//(index*100))
                if tmp < ans:
                    print ("ans(2) -> ",tmp,i,bit,index,score,-(-(G - score[0])//(index*100)),)
                    ans = tmp

    else:
        # 全問正解するパターン (0がない)
        score = f1(bit)
        print (bit, score)
        tmp = score[1]
        if tmp < ans:
            print ("ans(3) -> ",tmp,i,bit,score)
            ans = tmp

print (ans)
