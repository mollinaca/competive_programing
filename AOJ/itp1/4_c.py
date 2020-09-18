#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    a,op,b = map(str,input().split())
    if op == "?":
        exit ()
    else:
        if op == "/":
            print (int(a)//int(b))
        else:
            print (eval(a+op+b))