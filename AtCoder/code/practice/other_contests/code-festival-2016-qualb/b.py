#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,A,B = map(int,input().split())
s = input()
k = 0 # 予選通過人数
j = 0 # 予選通過した海外学生の人数
for x in s:
    if x == 'a':
        if k < A+B:
            print ('Yes')
            k += 1
        else:
            print ('No')
    elif x == 'b':
        if k < A+B and j < B:
            print ('Yes')
            k += 1
            j += 1
        else:
            print ('No')
    else: # x == 'c'
        print ('No')
