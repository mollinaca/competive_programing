#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
ans = ''
for x in range(len(s)):
    if s[x].isdigit():
        ans += s[x]
print (ans)
