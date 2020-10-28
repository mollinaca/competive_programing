#!/usr/bin/env python3
# -*- coding: utf-8 -*-
h1,m1,h2,m2,k = map(int,input().split())
x1 = 60*h1 + m1
x2 = 60*h2 + m2
print (-(k-(x2-x1)))
