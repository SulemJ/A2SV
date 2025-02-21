# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

d2=[]
for _ in range(5):
    n = list(map(int, input().split(" ")))
    d2.append(n)
for i in range(len(d2)):
    for j in range(len(d2[i])):
        if d2[i][j] == 1:
            print((abs(2-i)+abs(2-j)))