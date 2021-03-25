#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,X = map(int,input().split())
A = [a for a in list(map(int,input().split())) if a != X]
print(' '.join(map(str, A)))
