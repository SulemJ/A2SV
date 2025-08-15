# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

import sys
from functools import cache

sys.setrecursionlimit(10**6)

t = int(input())
l = list(map(int, input().split()))

@cache
def dp(i):
    if i == t - 1:
        return 0
    cost1 = abs(l[i+1] - l[i]) + dp(i+1)
    cost2 = float('inf')
    if i + 2 < t:
        cost2 = abs(l[i+2] - l[i]) + dp(i+2)
    return min(cost1, cost2)

print(dp(0))
