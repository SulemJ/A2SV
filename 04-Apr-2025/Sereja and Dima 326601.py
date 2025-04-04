# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

t=int(input())
n=list(map(int, input().split()))
l,r,s,d=0,len(n)-1,0,0
turn=True
while l<=r:
    if n[l]>=n[r]:
        if turn:
            s+=n[l]
            turn=False
        else:
            d+=n[l]
            turn=True
        l+=1
    else:
        if turn:
            s+=n[r]
            turn=False
        else:
            d+=n[r]
            turn=True
        r-=1
print(s,d)