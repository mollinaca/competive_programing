#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A = list(map(int,input().split()))

if len(set(A)) == 5:
    # 全部ばらばら
    print ("NO HAND")
    exit ()
if len(set(A)) == 4:
    # ちょうどふたつのみ
    print ("ONE PAIR")
    exit ()
elif len(set(A)) == 3:
    # ツーペア or スリーカード
    for i in set(A):
        if A.count(i) == 3:
            print ("THREE CARD")
            exit ()
    print ("TWO PAIR")
    exit ()
elif len(set(A)) == 2:
    # フルハウス or フォーカード
    for i in set(A):
        if A.count(i) == 3:
            print ("FULL HOUSE")
            exit ()

print ("NO HAND")
