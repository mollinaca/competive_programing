#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,k = map(int,input().split())
A = list(map(int,input().split()))
mod = (10**9)+7

# A そのものに含まれる転倒数
ans1 = 0
for i,a in enumerate(A):
    for j in range(i+1,len(A)):
        if j < a:
            ans1 += 1

# A[i]とA[j]の間の転倒数
ans2 = ans1
sortA = sorted(set(A))
d = {}
for i,a in enumerate(sortA):
    d[a] = i

for v in d.values():
    ans2 += v

print (ans1,ans2,d)
ans = ans1*k + ans2*((k*(k-1))//2)
print (ans%mod)
