#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
S = input()
ans = 0

for i in range(len(S)):
    if i == 0:
        ans += int(S)
    else:
        l = [x for x in range(len(S)-1)]
        for p in itertools.combinations(l,i):
            X = ''
            for si in range(len(S)):
                X += S[si]
                if si in p:
                    X += '+'
            ans += eval(X)

print (ans)
