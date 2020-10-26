#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
if len(s)%2 == 0:
    if "hi"*(len(s)//2) == s:
        print ("Yes")
        exit ()
print ("No")
