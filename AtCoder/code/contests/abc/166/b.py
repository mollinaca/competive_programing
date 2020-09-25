#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int,input().split())
l = list((range(1,n+1)))

for _ in range(k):
    d = int(input())
    A = list(map(int,input().split()))
    for i in A:
        if i in l:
            l.remove(i)

print (len(l))
