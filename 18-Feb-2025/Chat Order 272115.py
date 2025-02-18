# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

from collections import OrderedDict
t = int(input())
d =OrderedDict()
for _ in range(t):
    n = input()
    if n in d:
        del d[n]
    d[n]=None

for i in reversed(d):
    print(i)