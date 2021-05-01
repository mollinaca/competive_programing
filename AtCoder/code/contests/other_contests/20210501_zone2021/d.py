#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S = list(input())
T = ''
Rf = False
 
for s in S:
    if s == 'R':
        if Rf:
            Rf = False
        else:
            Rf = True
    elif not T:
        T += s
    else:
        if Rf:
            if T[0] == s:
                T = T[1::]
            else:
                T = s + T
        else:
            if T[-1] == s: 
                T = T[:-1]
            else:
                T += s
 
if Rf:
    print (T[::-1])
else:
    print (T)
