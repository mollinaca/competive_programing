#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
n = int(input())

def p (a:int,b:int):
    print (s[a:b+1])

def rev (a:int,b:int):
    tmp = s[a:b+1]
    return s[:a]+tmp[::-1]+s[b+1:]

def rep (a:int,b:int,p:str):
    return s[:a]+p+s[b+1:]

for _ in range(n):
    i = input().split()
    if i[0] == "print":
        p (int(i[1]),int(i[2]))
    elif i[0] == "reverse":
        s = rev (int(i[1]),int(i[2]))
    else:
        s = rep (int(i[1]),int(i[2]),i[3])
