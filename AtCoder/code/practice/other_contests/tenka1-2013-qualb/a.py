#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
S = []
for line in sys.stdin:
    S.append (line.rstrip())
S.sort()
print (S[6])
