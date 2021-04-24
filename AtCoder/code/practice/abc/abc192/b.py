#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S = input()
for i in range(len(S)):
    if i%2 == 0: # 先頭から奇数文字目
        if S[i].isupper():
            print ('No')
            exit ()
    else:
        if S[i].islower():
            print ('No')
            exit ()
print ('Yes')
