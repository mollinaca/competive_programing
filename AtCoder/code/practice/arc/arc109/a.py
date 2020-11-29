#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
a,b,x,y = map(int,input().split())
y2 = min(2*x,y)
d = abs((2*b)+1-(2*a))
print (math.floor(d/2)*y2 + x)
