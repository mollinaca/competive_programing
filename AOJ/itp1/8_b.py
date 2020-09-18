#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    n = int(input())
    if n == 0:
        exit ()
    else:
        print (sum(list(map(int, str(n)))))     
