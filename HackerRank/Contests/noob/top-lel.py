#!/usr/bin/env python3
# -*- coding: utf-8 -*-
L = list(input().split())
p = 0
for x in L:
    if x == "lol":
        p += 1
    elif x == "rofl":
        p += 2
    elif x == "lmao":
        p += 3
    elif x == "lel":
        p += 4
    else:
        pass

if 1 <= p <= 5:
    print ("Patient has bright red face")
elif 6 <= p <= 12:
    print ("Patient is unable to speak")
elif 13 <= p <= 20:
    print ("Patient's sides are mildly bruised")
elif 21 <= p <= 30:
    print ("Patient has broken jaw, fractured ribs")
elif 31 <= p <= 49:
    print ("Patient is in a coma")
else:
    print ("Patient is dead")
