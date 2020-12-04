#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c = map(int,input().split())
ans = 0

if a%2 == 1 or b%2 == 1 or c%2 == 1:
    print (ans)
    exit ()

if a == b == c:
    print (-1)
    exit ()

while True:
    ans += 1
    a2 = a//2
    b2 = b//2
    c2 = c//2
    new_a = b2 + c2
    new_b = a2 + c2
    new_c = a2 + b2

    if new_a%2 == 1 or new_b%2 == 1 or new_c%2 == 1:
        print (ans)
        exit ()
    
    a = new_a
    b = new_b
    c = new_c
