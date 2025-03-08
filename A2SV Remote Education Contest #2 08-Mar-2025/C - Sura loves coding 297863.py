# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C

t = int(input())
n = input()
arr =[]
for i in reversed(n):
    idx = len(arr)//2
    arr.insert(idx, i)
print("".join(arr))