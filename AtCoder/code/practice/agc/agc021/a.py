#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
if len(s) == s.count('9'):
    print (9*len(s))
elif s[0] != '9' and s.count('9') == len(s)-1:
    print (int(s[0])+9*(len(s)-1))
else:
    print (int(s[0])+9*(len(s)-1)-1)
