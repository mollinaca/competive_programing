#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
S = set()
S_ = set()

for _ in range(N):
    s = input()
    if "!" in s:
        if s in S_:
            pass
        else:
            S_.add(s)
    else:
        if s in S:
            pass
        else:
            S.add(s)

for s in S:
    if "!"+s in S_:
        print (s)
        exit ()

print ("satisfiable ")
