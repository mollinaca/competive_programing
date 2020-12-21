#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())*2

def check (l:list):
    c0 = 0
    c1 = 0
    for x in l:
        if x == 0:
            c0 += 1
        else: # x == 1:
            c1 += 1
            if c1 < c0:
                pass
            elif c1 == c0:
                c0 = 0
                c1 = 0
                continue
            else: # c0 < c1:
                return False
    else:
        return True

ans = 0
for i in range(2**n):
    bit = [0]*n
    for j in range(n):
        if ((i>>j)&1):
            bit[n-1-j] = 1

    # 処理
    if not bit.count(0) == bit.count(1):
        continue

    if check (bit):
        ans += 1

print (ans)
