#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
task_time = {}
task_limit = {}
for i in range(1,n+1):
    a,b = map(int,input().split())
    task_time[i] = a
    task_limit[i] = b

task_limit_sorted = sorted(task_limit.items(), key=lambda x:x[1])

time = 0
for i in task_limit_sorted:
    time += task_time[i[0]]
    if task_limit[i[0]] < time:
        print ("No")
        exit ()

print ("Yes")
