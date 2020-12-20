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
    t = []
    for j in range(N):
        if ((i>>j)&1):
            t.append(j+1)

    # t の人が正直と仮定
    tmp = len(t)
    f = True
    for q in range(1,N+1):
        if q in t: # q は親切と仮定
            # 正直で矛盾がないかチェック 矛盾があれば f を Falseにする
            # XY を確認し、「正直な人」が k は 1 であると言っていればOK、0であると言っていれば矛盾
            for k,v in XY.items():
                if k in t: # kは正直と仮定
                    for v1,v2 in v.items():
                        if not v1 == q:
                            pass
                        else:
                            if v2 == 0:
                                # q == v1 は親切と仮定したが不親切だった -> 矛盾
                                f = False
                                break
                else: # k は不親切と仮定
                    pass # k の証言は無視する
        else: # q は不親切と仮定
            # 不親切で矛盾がないかチェック 矛盾があれば f を Falseにする
            # XY を確認し、「正直な人」が k は 0 であると言っていればOK、1であると言っていれば矛盾
            for k,v in XY.items():
                if k in t: # k は正直と仮定
                    for v1,v2 in v.items():
                        if not v1 == q:
                            pass
                        else:
                            if v2 == 1:
                                # q == v1 は不親切と仮定したが正直だった -> 矛盾
                                f = False
                                break
                else: # k は不親切と仮定
                    pass # k の証言は無視する

    if f:
        if ans < tmp:
            ans = tmp

print (ans)
