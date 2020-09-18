#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

# p = 1
ans = 0
for i in range(n):
    ans += abs(x[i]-y[i])
print (ans)

# p = 2
ans = 0
for i in range(n):
    ans += (abs(x[i]-y[i]))**2
print (ans**(1/2))

# p = 3
ans = 0
for i in range(n):
    ans += (abs(x[i]-y[i]))**3
print (ans**(1/3))

# p = inf
ans = []
for i in range(n):
    ans.append(abs(x[i]-y[i]))
print (max(ans))
