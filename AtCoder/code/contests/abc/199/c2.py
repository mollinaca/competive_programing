#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N = int(input())
S = list(input())
Q = int(input())
l = [i for i in range(1,(2*N)+1)]

for _ in range(Q):
    T,A,B = map(int,input().split())
    s = []
    if T == 1:
        if A == 1 and B == 2*N:
            s.append(l[B-1])
            s.append(l[A:B-1])
            s.append(l[A-1])
            l = []
            for s2 in s:
                if type(s2) == list:
                    for s3 in s2:
                        l.append(s3)
                else:
                    l.append(s2)

        elif A == 1:
            s.append(l[B-1])
            s.append(l[1:B-1])
            s.append(l[A-1])
            s.append(l[B::])
            l = []
            for s2 in s:
                if type(s2) == list:
                    for s3 in s2:
                        l.append(s3)
                else:
                    l.append(s2)

        elif B == 2*N:
            s.append(l[0:A-1])
            s.append(l[B-1])
            s.append(l[A:B-1])
            s.append(l[A-1])
            l = []
            for s2 in s:
                if type(s2) == list:
                    for s3 in s2:
                        l.append(s3)
                else:
                    l.append(s2)

        else:
            s.append(l[0:A-1])
            s.append(l[B-1])
            s.append(l[A:B-1])
            s.append(l[A-1])
            s.append(l[B::])
            l = []
            for s2 in s:
                if type(s2) == list:
                    for s3 in s2:
                        l.append(s3)
                else:
                    l.append(s2)

    else: # T == 2:
        s.append(l[N::])
        s.append(l[0:N])
        l = []
        for s2 in s:
            for s3 in s2:
                l.append(s3)

for x in l:
    print (S[x-1],end='')
