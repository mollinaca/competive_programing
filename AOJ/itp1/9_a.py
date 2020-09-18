#!/usr/bin/env python3
# -*- coding: utf-8 -*-
w = input()
T = []

while True:
    t = list(input().split())
    if t == ['END_OF_TEXT']:

        break
    else:
        t = [s.lower() for s in t]
        T.append(t)

total = 0
for line in T:
    total += line.count(w.lower())

print (total)
