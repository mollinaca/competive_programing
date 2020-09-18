#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n, m = map(int, input().split())
A = []
b = []

for i in range(n):
    A.append([int(s) for s in input().split()])

for i in range(m):
    b.append([int(input())])

for i in range(n):
    sum_i = 0
    for j in range(m):
        sum_i += A[i][j] * b[j][0]

    print(sum_i)