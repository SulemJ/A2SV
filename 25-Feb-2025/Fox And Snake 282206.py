# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A


n,m=map(int,input().split(" "))
a=[]
t=True
for i in range(n):
    if i %2==0:
        a.append("#"*(m))

    else:
        if t==True:
            s="."*(m-1)+"#"
            t=False
        else:
            s="#"+"."*(m-1)
            t=True
        a.append(s)


for i in a:
    print(i)

