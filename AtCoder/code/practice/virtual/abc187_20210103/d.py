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
print (l)

ans = 0
t = 0 # 高橋派は最初0
for d in l:
    c = d['city']
    a = a - d['a']
    t = t + d['a'] + d['t']
    ans += 1
    print (d['city'],a,t)

    if a < t:
        print (ans)
        exit ()
