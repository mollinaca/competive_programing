#!/usr/bin/env python3
# -*- coding: utf-8 -*-
K = int(input())
a = 0
for i in range(1,K+1):
    a = ((a%K)*10)+7
    if a%K == 0:
        print (i)
        exit ()
print (-1)
