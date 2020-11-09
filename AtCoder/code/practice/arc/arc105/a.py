#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = sorted(list(map(int,input().split())))
if l[0] + l[3] == l[1] + l[2] or l[0] + l[1] + l[2] == l[3]:
    print ('Yes')
else:
    print ('No')
