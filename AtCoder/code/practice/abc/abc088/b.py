#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
a = sorted(list(map(int,input().split())), reverse=True)
alice = 0
bob = 0
for i in range(len(a)):
    if i%2 == 0:
        alice += a[i]
    else:
        bob += a[i]
print (alice-bob)
