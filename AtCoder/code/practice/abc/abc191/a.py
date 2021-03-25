#!/usr/bin/env python3
# -*- coding: utf-8 -*-
V,T,S,D = map(int,input().split())
print ('No') if T <= D/V <= S else print ('Yes')
