# Problem: D - Pirates Island: Painting the Grand Line - https://codeforces.com/gym/594356/problem/D

import sys 
input = sys.stdin.readline 

t=int(input())
for _ in range(t):
    n,m = map(int, input().split())
    grid= [list(map(int, input().split())) for i in range(n)]
    colors=[0]*(n*m+1)
    neigbours=[0]*(n*m+1)
    for i in range(n):
        for j in range(m):
            colors[grid[i][j]]=1
            if i+1<n and grid[i][j]==grid[i+1][j]:
                neigbours[grid[i][j]]=1
            if j+1<m and grid[i][j]==grid[i][j+1]:
                neigbours[grid[i][j]]=1
    print(sum(colors)-1+sum(neigbours)-max(neigbours))