#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b = map(int,input().split())
if a*b == 15:
    print ('*')
elif a+b == 15:
    print ('+')
else:
    print ('x')
