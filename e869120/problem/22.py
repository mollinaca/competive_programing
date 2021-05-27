#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a,b,c = map(int,input().split())

import math
from functools import reduce
def gcd_list(numbers:list) -> int:
    return reduce(math.gcd, numbers)

g = gcd_list([a,b,c])
ans = 0
for x in [a,b,c]:
    ans += (x//g)-1
print (ans)
