#!/usr/bin/env python3
# -*- coding: utf-8 -*-
K = int(input())

X = 0
for i in range(1,K+1):
    X = 10*X + 7
    if X%K == 0:
        print (i)
        exit ()
print (-1)
