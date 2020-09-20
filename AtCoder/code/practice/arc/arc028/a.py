#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n,a,b = map(int,input().split())
x = n%(a+b)
print ("Ant") if 1 <= x <= a else print ("Bug")
