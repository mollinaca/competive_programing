#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
Q = int(input())

bag = {}
bag_key = deque()
ans = []
for _ in range(Q):
#    print ("bag_key:",bag_key)
#    print ("bag:",bag)

    Px = list(map(int,input().split()))
    if Px[0] == 1:
        X = Px[1]
        if X not in bag:
            bag[X] = 1
            bag_key.append(X)
        else:
            bag[X] += 1
    elif Px[0] == 2:
        X = Px[1]
        for k in sorted(bag.keys(), reverse=True):
            bag[k+X] = bag[k]
            bag[k] = 0
        bag_key = deque([i+X for i in bag_key])

    else: # P == 3
        sorted(bag_key)
        ans.append(bag_key[0])
        bag[bag_key[0]] -= 1
        if bag[bag_key[0]] == 0:
            bag_key.popleft()

for a in ans:
    print (a)
