#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))

def bubbleSort(l:list, n:int):
    count = 0
    flag = True
    while flag:
        flag = False
        for j in range(n-1, 0, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
                flag = True
                count += 1
    return count

ans = bubbleSort (l,n)
print (' '.join(map(str, l)))
print (ans)
