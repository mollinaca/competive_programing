#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
a,b,C=map(float,input().split())

s=math.radians(C)
h=b*math.sin(s)
S=(a*h)/2
c=math.sqrt(a**2+b**2-2*a*b*math.cos(s))
L=a+b+c
print(S,L,h,sep="\n")
