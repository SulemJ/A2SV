# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

n, m = map(int, input().split())
degree = [0]*n 

for i in range(m):
    a,b = map(int, input().split())
    degree[a-1]+=1
    degree[b-1]+=1
print("YES") if all(d==degree[0] for d in degree) else print("NO")
