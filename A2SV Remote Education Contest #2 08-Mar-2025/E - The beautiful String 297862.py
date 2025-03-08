# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

t = int(input())
# n=int(n)
for _ in range(t):
    n = input()
    arr = [i for i in n]
    count=0
    target = ["1", "1", "0", "0"]
    i=0
    while i < len(arr):
        if arr[i:i+4] == target:
            count+=1
            i+=4
        else:
            i+=1       
    x = int(input())
    for _ in range(x):
        a, b = map(int, input().split(" "))
        prev,cur= 0,0
        a-=1
        if (a-3 >= 0 and arr[a-3:a+1] == target) or (a-2 >= 0 and a+1<len(arr) and arr[a-2:a+2] == target) or (a-1 >= 0 and a+2<len(arr) and arr[a-1:a+3] == target) or (a+3<len(arr) and arr[a:a+4] == target): 
            prev =1
        arr[a] = str(b)
        if (a-3 >= 0 and arr[a-3:a+1] == target) or (a-2 >= 0 and a+1<len(arr) and arr[a-2:a+2] == target) or (a-1 >= 0 and a+2<len(arr) and arr[a-1:a+3] == target) or (a+3<len(arr) and arr[a:a+4] == target): 

            cur =1
        # print("".join(arr))
        count+=cur-prev
        if count:           # if "1100" in "".join(arr):
            print("YES")
        else:
            print("NO")