#!/usr/bin/env python3
# -*- coding: utf-8 -*-
K = int(input())

def j (x:int) -> bool:
    for i in range(len(str(x))-1):
        if 1 < abs(int(str(x)[i])-int(str(x)[i+1])):
            return False
    return True

c = 0
i = 0
while True:
    i += 1
    if j(i):
        c += 1
    
    if c == K:
        print (i)
        exit ()
