#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = input()
if s == 'keyence':
    print ("YES")
    exit ()
elif not 'k' in s:
    print ("NO")
    exit ()
else:
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[0:i]+s[j::] == 'keyence':
                print ('YES')
                exit ()

print ('NO')
