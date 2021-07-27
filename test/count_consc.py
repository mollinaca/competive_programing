#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = list(map(int,input().split()))

# 1 が連続する最大の回数を出力する
def c (l:list) -> int:
    ret = 0
    t = 0
    for x in l:
        if x == 0:
            t += 1
        else:
            ret = max(t,ret)
            t = 0
    else:
        ret = max(t,ret)

    return ret
