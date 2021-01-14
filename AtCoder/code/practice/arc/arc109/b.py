#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

if n == 1 or n == 2:
    print (1)
    exit ()
else:
    pass

def calc (p:int):
    return (p*(p+1))//2

l = 1
u = n
x = (l+u)//2
while True:
    if calc(x) <= n+1 < calc(x+1):
        break
    else:
        if calc(x) < n+1:
            l = x
            x = (l+u)//2
        else: # n+1 < calc(x)
            u = x
            x = (l+u)//2

# 長さ n+1 を1本買うと、1,,,x までの x 本が手に入る
# 残り x+1 ~ n は1本ずつ買う
print (n-x+1)
