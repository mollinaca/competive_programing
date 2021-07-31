#!/usr/bin/env python3
# -*- coding: utf-8 -*-
A,B = map(int,input().split())

if 0 < A and 0 < B:
    print ("Alloy")
elif B == 0:
    print ("Gold")

elif A == 0:
    print ("Silver")
else:
    pass
