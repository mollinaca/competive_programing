#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))

def selectionSort(A:list, N:int):
    count = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if not A[i] == A[minj]:
            A[i], A[minj] = A[minj], A[i]
            count += 1
    
    return A, count

l, ans = selectionSort(l,n)
print(' '.join(map(str, l)))
print (ans)
