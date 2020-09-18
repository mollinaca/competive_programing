#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(input().split())
print ("YES") if len(l) == len(set(l)) else print ("NO")
