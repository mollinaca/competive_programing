#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c = input().split()
print ("YES") if a[-1] == b[0] and b[-1] == c[0] else print ("NO")
