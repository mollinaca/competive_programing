#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
p = input()
s = s+s+s
print ("Yes") if s.count(p) >= 1 else print ("No")
