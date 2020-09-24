#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())

def isPrime (x:int) -> bool:
  if x == 1:
    return False
  d = int(x**(1/2)) + 1
  for i in range(2,d):
    if x % i == 0:
      return False
  return True

if isPrime(n):
    print ("Prime")
else:
    if n == 1:
        print ("Not Prime")
    elif (not int(str(n)[-1])%2 == 0) and (not str(n)[-1] == '5') and (not n%3 == 0):
        print ("Prime")
    else:
        print ("Not Prime")
