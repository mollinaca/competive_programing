#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
l = list(map(int,input().split()))
l2 = [n for n in l if n%2 != 0]
print ("YES") if len(l2)%2 == 0 else print ("NO")
