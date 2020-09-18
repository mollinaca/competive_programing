#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    n = int(input())
    if n == 0:
        exit ()
    else:
        S = list(map(int,input().split()))
        m = sum(S)/n
        sigma = 0
        for i in S:
            sigma += (i-m)**2
        print ((sigma/n)**0.5)
