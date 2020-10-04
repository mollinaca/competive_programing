#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
ans = 1
while True:
    if (ans*n)%360 == 0:
        print (ans)
        exit ()
    ans += 1
