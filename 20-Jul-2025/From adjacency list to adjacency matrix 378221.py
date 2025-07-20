# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
ans=[[0 for i in range(n)] for _ in range(n)]
for i in range(n):
    a=list(map(int, input().split()))
    for j in range(1,len(a)):
        ans[i][a[j]-1]+=1
for l in ans:
    for x in l:
        print(x,end=" ")
    print()