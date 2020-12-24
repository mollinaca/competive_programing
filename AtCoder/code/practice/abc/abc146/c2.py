#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A,B,X = map(int,input().split())

def p (n:int):
    return A*n + B*(len(str(n)))

low = 0
high = 10**9

if p(high) <= X:
    print (high)
    exit()
elif X <= p(low):
    print (low)
    exit ()
else:
    pass

while True:
    avg = (high+low)//2

    if p(avg) <= X and X < p(avg+1):
        print (avg)
        exit ()
    else:
        if p(avg) <= X:
            low = avg
        else:
            high = avg
