#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))

def judge (a,b,c):
    if a < b+c and b < a+c and c < a+b and not a == b and not b == c and not a == c:
        return True
    else:
        return False

ans = 0
for i in range(n-2):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if judge(l[i],l[j],l[k]):
                ans += 1

print (ans)
