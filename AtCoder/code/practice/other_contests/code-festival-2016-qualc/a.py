#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S = input()
for i in range(len(S)):
    if S[i] == 'C':
        for j in range(i+1,len(S)):
            if S[j] == 'F':
                print ('Yes')
                exit ()
print ('No')
