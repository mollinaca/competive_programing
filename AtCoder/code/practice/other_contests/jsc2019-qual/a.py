#!/usr/bin/env python3
# -*- coding: utf-8 -*-
M,D = map(int,input().split())
ans = 0
for m in range(1,M+1):
    for d in range(22,D+1):
        if int(str(d)[1]) < 2:
            pass
        else:
            if int(str(d)[0])*int(str(d)[1]) == m:
                ans += 1
print (ans)
