#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r,g,b = input().split()
print ("YES") if int(r+g+b)%4 == 0 else print ("NO")
