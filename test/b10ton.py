#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def B10toN(X,N):
    if (int(X/N)):
        return B10toN(int(X/N), N)+str(X%N)
    return str(X%N)

n = int(input())
print (B10toN(n,2))

