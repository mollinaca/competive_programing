#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = {}
XY = {}

for i in range(1,N+1):
    n = int(input())
    A[i] = n
    d = {}
    for _ in range(n):
        x,y = map(int,input().split())
        d[x] = y
    XY[i] = d

ans = 0
for i in range(2**N):
    bit = [0]*N
    for j in range(N):
        if ((i>>j)&1):
            bit[N-1-j] = 1

#    print (bit) # 0 が不親切、1が親切。indexが0始まりに注意（人1→indexが0）

    # 矛盾がないか調べる
    f = True # 矛盾してたらここを False にしてパターンの調査を終了する
    for k,v in XY.items():
#        print ("k,v:",k,v)
        if bit[k-1] == 0: # k は不親切と仮定してるので証言を無視する
            pass
        else:
            for v1,v2 in v.items():
                if not bit[v1-1] == v2: # 矛盾
                    f = False
                    break

    if f:
        t = bit.count(1)
        if ans < t:
            ans = t

print (ans)
