#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        leap = True
    return leap

year = int(input())
