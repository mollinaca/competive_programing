#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sf (l:str, x:int):
    return (l[x:]+l[:x])

while True:
    s = input()
    if s == "-": break

    m = int(input())
    for _ in range(m):
        h = int(input())
        s = sf (s,h)

    print (s)
