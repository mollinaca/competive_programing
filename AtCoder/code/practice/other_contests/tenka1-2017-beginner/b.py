#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = []
d = {}
for _ in range(n):
    n,m = map(int,input().split())
    d[n] = m
    l.append(n)

print (max(l)+d[max(l)])
