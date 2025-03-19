# Problem: Books - https://codeforces.com/contest/279/problem/B

def solve():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
#1 1 2 3
    k=0
    c=0
    l=0
    for r in range(n):
        c+=a[r]
        if c >m:
            c-=a[l]
            l+=1
        k=max(k,r-l+1)
    return k
if __name__ == '__main__':
    # for _ in range(int(input())):
    
    print(solve())