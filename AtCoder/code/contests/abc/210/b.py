#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
S = input()

for i,s in enumerate(S):
    if s == '1':
        if i%2 == 0:
            print ('Takahashi')
        else:
            print ('Aoki')
        exit ()
