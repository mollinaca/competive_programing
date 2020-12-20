#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c,k = map(int,input().split())
if k <= a:
    print (k)
elif a < k <= a+b:
    print (a)
elif a+b < k <= a+b+c:
    print (a-(k-(a+b)))
else:
    print (a-b)
