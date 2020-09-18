#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
c = 0

def isPrime(x:int):
    if x < 2 or x == 9:
        return False
    if x == 2 or x == 3:
        return True
    if x%2 == 0:
        return False
    i = 2
    while True:
        i += 1
        if x%i == 0:
            return False
        if x <= i**2 :
            return True

for _ in range(n):
    if isPrime(int(input())):
        c += 1

print (c)
