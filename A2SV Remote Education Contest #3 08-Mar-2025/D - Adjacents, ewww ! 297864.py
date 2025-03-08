# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2:
        print(-1)
    elif n == 1:
        print(1)
    else:
        d2 = [[0] * n for _ in range(n)]
        odd=1
        even=2
        limit=n*n
        for i in range(n):
            for j in range(n):
                if odd <=limit:
                    d2[i][j]=odd
                    odd+=2
        for i in range(n):
            for j in range(n):
                if d2[i][j] == 0 and even <=limit:
                    d2[i][j]=even
                    even+=2
        for i in d2:
            print(*i)