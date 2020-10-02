#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A,K = map(int,input().split())
ans = 0

if K == 0:
    ans = 2*(10**12)-A
    print (ans)
    exit ()

while True:
    ans += 1
    A += 1 + K*A
    if 2*(10**12) <= A:
        print (ans)
        exit ()
