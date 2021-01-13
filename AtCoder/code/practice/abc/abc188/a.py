#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x,y = map(int,input().split())
print ('Yes') if max(x,y) < min(x,y)+3 else print ('No')
