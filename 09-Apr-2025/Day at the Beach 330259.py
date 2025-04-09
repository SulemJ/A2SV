# Problem: Day at the Beach - https://codeforces.com/problemset/problem/599/C

t=int(input())
h=list(map(int, input().split()))
prf=[h[0]]
for i in range(1,t):
    prf.append(max(prf[-1],h[i]))
sfx=[0]*t
sfx[t-1]=h[t-1]
for i in range(t-2,-1,-1):
    sfx[i]=min(sfx[i+1],h[i])
c=1
for i in range(t-1):
    if prf[i]<=sfx[i+1]:
        c+=1
print(c)