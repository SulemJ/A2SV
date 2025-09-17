# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

t= int(input())
list=[0]*(t+1)
for i in range(2, t):
    if list[i]==0:
        for j in range(i, t+1,i):
            list[j]+=1
s=0
for x in list:
    if x ==2:
        s+=1
print(s)