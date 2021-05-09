#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
A,B,C = sorted(map(int,input().split()))
ans = 9999

for x in range((N//A)+1):
    for y in range(((N-A*x)//B)+1):
        if N < A*x + B*y:
            break

        if (N-A*x-B*y)%C == 0:
            z = (N-A*x-B*y)//C
            ans = min(ans,x+y+z)

print (ans)
