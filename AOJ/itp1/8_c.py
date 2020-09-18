#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
s = []
for line in sys.stdin:
    s.append (list(line.rstrip()))

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
for x in alphabet:
    t = 0
    for l in s:
        t += l.count(x)+l.count(str.upper(x))
    print (x,":",t)
