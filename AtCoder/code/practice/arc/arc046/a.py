#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
count = 0

def j (x:int) -> bool:
    p = ''
    for i in range(len(str(x))):
        if i == 0:
            p = str(x)[i]
        else:
            if not str(x)[i] == p:
                return False
    return True

for i in range(1,10**9):
    if j(i):
        count += 1
        if count == n:
            print (i)
            exit ()
