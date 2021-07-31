#!/usr/bin/env python3
# -*- coding: utf-8 -*-
p = input()

if p[0] == p[1] == p[2] == p[3]:
    ans = "Weak"
else:
    if (int(p[0])+1 == int(p[1]) or int(p[0])-9 == int(p[1])) and (int(p[1])+1 == int(p[2]) or int(p[1])-9 == int(p[2])) and (int(p[2])+1 == int(p[3]) or int(p[2])-9 == int(p[3])):
        ans = "Weak"
    else:
        ans = "Strong"

print (ans)
