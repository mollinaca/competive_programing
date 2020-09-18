#!/usr/bin/env python3
# -*- coding: utf-8 -*-
while True:
    n,x = map(int,input().split())
    if n == 0 and x == 0:
        exit ()
    
    count = 0

    for i in range(1,n+1):
        for j in range(2,n+1):
            if j <= i:
                pass
            else:
                for k in range(3,n+1):
                    if k <= j or k <= i:
                        pass
                    else:
                        if i+j+k == x:
                            count += 1
    print (count)
