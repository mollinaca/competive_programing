#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
s = input()
W = [0]
E = [0]

for i in range(len(s)):
    if s[i] == 'W':
        W.append(W[i]+1)
    else:
        W.append(W[i])
    
    if s[-(i+1)] == 'E':
        E.append(E[i]+1)
    else:
        E.append(E[i])

W.append(0)
E.append(0)
E.reverse()

ans = float('inf')
for i in range(1,n+1):
    ans = min(ans,W[i-1]+E[i+1])

print (ans)
