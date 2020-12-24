#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
L = sorted(list(map(int,input().split())))

def judge(a,b,n:int):
    if a+b <= n:
        return False
    else:
        return True

ans = 0
for i,a in enumerate(L):
    for j,b in enumerate(L[i+1::]):
        l = L[i+j+2::]
        if len(l) == 0:
            continue
        elif len(l) == 1:
            if judge(a,b,l[0]):
                ans += 1
                continue
            else:
                continue
        else:
            low = 0
            high = len(l)

            if judge(a,b,l[-1]):
                ans += len(l)
                continue
            elif not judge(a,b,l[0]):
                continue
            else:
                while True:
                    avg = (low+high)//2
                    if low == high:
                        break
                    if judge(a,b,l[avg]) and not judge(a,b,l[avg+1]): # 境界
                        ans += avg+1
                        break
                    else:
                        if l[avg] < a+b:
                            low = avg
                        else: # a+b <= l[avg]:
                            high = avg

print (ans)
