# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())
ans=0
for i in range(n):
    s = list(map(int, input().split()))
    ans+=sum(s)
print (ans//2)
