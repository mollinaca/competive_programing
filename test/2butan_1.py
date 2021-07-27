#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 例えばこういうリスト
L = [1,3,6,10,15,46,57,89,153,175,236,358,359,560,667,801,9634,16367]

# ここから、 "任意の値より小さい最大の整数" をにぶたんする

x = int(input())

l = 0
r = len(L)

# このサーチは、対象 x が L の中にあることが前提
while True:
    mid = (l+r)//2
    print (L,l,mid,r)

    if L[mid] < x and x <= L[mid+1]:
        print (L[mid])
        break
    else:
        if x <= L[mid]:
            r = mid
        else:
            l = mid
