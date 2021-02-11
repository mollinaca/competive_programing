#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
n = int(input())

bugs = []
for line in sys.stdin:
    l = list(line.split())
    for x in l:
        bugs.append (int(x))

lv = 1
HP = 10
killed = 0

for buglv in bugs:
    print ("battle buglv:",buglv,"HP:",HP)

    if lv < buglv:
        dmg = buglv*2
    elif lv == buglv:
        dmg = buglv
    else: # buglv < lv
        dmg = 1
    HP -= dmg

    if HP <= 0:
        print ("You have died. Reached level",lv,"and killed",killed,"bugs")
        exit ()
    killed += 1

    if killed%3 == 0: # lv up
        lv += 1
        HP = (lv+1)*5
        print ("lv up reached",lv,"with",HP)

    print ("you fighet bug:",buglv,",lose hp:",dmg,",hp left:",HP)

print ("You have won! Reached level",lv,"and killed",killed,"bugs")
