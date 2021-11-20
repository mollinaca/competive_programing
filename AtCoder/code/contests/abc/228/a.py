#!/usr/bin/env python3
# -*- coding: utf-8 -*-
S,T,X = map(int,input().split())

# 日付をまたぐかどうか
if T < S: # またぐ
    if S <= X or X < T:
        print ("Yes")
    else:
        print ("No")

else: # またがない
    if S <= X < T:
        print ("Yes")
    else:
        print ("No")
