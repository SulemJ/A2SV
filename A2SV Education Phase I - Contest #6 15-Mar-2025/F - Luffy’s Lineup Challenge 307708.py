# Problem: F - Luffy’s Lineup Challenge - https://codeforces.com/gym/594356/problem/F

n = int(input())
a = list(map(int,input().split()))        # a=[1,2,3,2] 
b = list(map(int, input().split())) 
def targetInB(start,aOfi):
    for i in range(start,n):
        if b[i] == aOfi:
            return i
r=[]
for i in range(n):
    aOfi=a[i]
    bOfi=targetInB(i,aOfi)
    # print(aOfi,bOfi)
    while bOfi>i:
        r.append([bOfi,bOfi+1])
        b[bOfi],b[bOfi-1]=b[bOfi-1],b[bOfi]
        bOfi-=1
print(len(r))
for i in r:
    print(*i)