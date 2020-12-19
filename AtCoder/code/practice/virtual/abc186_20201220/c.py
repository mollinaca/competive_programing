#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

def j (p:int) -> bool:
    if '7' in str(oct(p)):
        return True
    else:
        return False

ans = 0
for i in range(1,n+1):
    if '7' in str(i):
        continue
    else:
        if j(i):
            continue
        else:
            ans += 1

print (ans)
