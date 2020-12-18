#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(input())
op = ['+','-']

for op1 in op:
    for op2 in op:
        for op3 in op:
            X = l[0] + op1 + l[1] + op2 + l[2] + op3 + l[3]
            if eval(X) == 7:
                print (X+"=7")
                exit ()
