# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

n, t = map(int, input().split())

start = 10**(n-1)

num = (start + t - 1) // t * t

if len(str(num)) == n:
    print(num)
else:
    print(-1)