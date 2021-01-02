#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())

l = []
t = 0
a = 0
for i in range(1,N+1):
    A,B = map(int,input().split())
    d = {"city":i,"a":A,"t":B}
    l.append(d)
    a += A
    t += B

import operator
l = sorted(l, key=operator.itemgetter('a','t'), reverse=True)

ans = 0
X = 0-a
for d in l:
    X += 2*d['a'] + d['t']
    ans += 1
    if 0 < X:
        print (ans)
        exit ()
