#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
if n <= 59:
    print ('F')
elif 60 <= n <= 69:
    print ('D')
elif 70 <= n <= 79:
    print ('C')
elif 80 <= n <= 89:
    print ('B')
else:
    print ('A')
