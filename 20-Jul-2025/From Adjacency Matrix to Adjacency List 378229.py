# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

n = int(input())
ans=[[0] for i in range(n)]
for i in range(n):
    s = list(map(int, input().split()))
    for j in range(n):
        if s[j]==1:
            ans[i][0]+=1
            ans[i].append(j+1)

for i in ans:
    for j in i:
        print(j,end=(" "))
    print()