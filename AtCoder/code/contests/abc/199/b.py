#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
mA = max(A)
mB = min(B)
print (max(0,mB-mA+1))
