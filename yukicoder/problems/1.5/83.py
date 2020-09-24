#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
if n%2 == 0:
    print ('1'*(n//2))
elif n == 3:
    print (7)
else:
    print ('7'+'1'*((n//2)-1))
