#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b = input().split()
a_change = max (int('9' + a[1] + a[2]), int(a[0] + '9' + a[2]), int(a[0] + a[1] + '9'))
b_change = min (int('1' + b[1] + b[2]), int(b[0] + '0' + b[2]), int(b[0] + b[1] + '0'))
print (max(int(a)-b_change, a_change-int(b)))
