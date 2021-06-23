#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
q = deque()

while True:
    print ("q:",q)
    print ("append -> a, pop -> r, popleft -> l:", end="")
    s = input()

    if s == "a":
        print ("add num: ", end="")
        n = int(input())
        q.append(n)
    elif s == "r":
        q.pop()
    elif s == "l":
        q.popleft()
    else:
        print ("invalied")
        exit ()
