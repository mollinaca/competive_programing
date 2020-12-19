#!/usr/bin/env python3
# -*- coding: utf-8 -*-
N,M = map(int,input().split())
k = []
s = {}
for i in range(1,M+1):
    l = list(map(int,input().split()))
    k.append(l[0])
    s[i] = l[1::]

p = list(map(int,input().split()))

ans = 0
# N個のスイッチのON/OFFパターン
for i in range(2**N):
    switch = []
    for j in range(N):
        if ((i>>j)&1):
            switch.append(j+1)

#    print ("点灯パターン：", switch) # ONになっているスイッチの番号
    f = False

    # 電球 x が ON になるかどうか
    for x in range(1,M+1):
#        print ("電球:",x,"s[x]:",s[x],"p ->",p[x-1])
        # 対象のスイッチのうちONになってるものの個数
#        print ("対象のスイッチ:",s[x])
        count = 0 # 対象のスイッチのうちONになってるものの個数
        for ts in s[x]:
            if ts in switch:
                count += 1
#        print ("対象のスイッチのうちONになってるものの数:",count)

        if not count%2 == p[x-1]:
#            print ("OFF")
            f = True

    if f:
        continue

    # このパターンではすべての電球がONだった
    ans += 1

print (ans)
