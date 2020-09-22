#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(input().split())
n = int(input())

def check(x:str, y:str) -> bool:
    if len(x) != len(y):
        return False
    
    for a, b in zip(x,y):
        if a == "*" or b =="*":
            pass
        else:
            if a != b:
                return False

    return True

for _ in range(n):
    w = input()

    for i, words in enumerate(l):
        if check (words, w):
            l[i] = "*"*len(words)

print(' '.join(map(str, l)))
