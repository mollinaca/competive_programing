#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = [0] * 10*12

for _ in range(n):
    b,f,r,v = map(int,input().split())
    k = 3*10*(b-1) + 10*(f-1) + (r-1)
    l[k] = l[k] + v

k = 0
for i in range(15):
    if (i+1)%4 == 0:
        print ('####################')
        k += 1
    else:
        for j in range(10):
            print (' ' + str(l[((0+i-k)*10)+j]), end='')
        print ()
