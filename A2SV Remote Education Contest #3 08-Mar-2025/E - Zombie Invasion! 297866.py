# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

from collections import defaultdict
def solve():
    n, k= map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    mp= defaultdict(int)
    for i in range(n):
        mp[abs(b[i])]+=a[i]
    # print(zdb)
    l =1
    for i in range(n+1):  #i=0 l=1
        tmp=k
        if l==i and mp[l]>0:
            print("NO")
            return
        while tmp>0 and l<=n:
            if mp[l]>=tmp:
                mp[l]-=tmp
                tmp=0
            elif mp[l]<tmp:
                tmp-=mp[l]
                mp[l]=0
                l+=1
        if l>n:
            break
    print("YES")                 

t= int(input())
for _ in range(t):
    h = solve()