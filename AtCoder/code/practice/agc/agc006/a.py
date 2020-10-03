#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
s = input()
t = input()

if s == t:
    print (len(s))
else:
    for i in range(n):
        if s[i::] == t[0:-i]:
            x = n-i
            print (2*n-x)
            exit ()
    else:
        print (2*n)
