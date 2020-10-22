#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
w = s.count('o')
print ('YES') if 8 <= w+(15-len(s)) else print ('NO')
