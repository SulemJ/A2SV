# Problem: E - Straw Hat's Blue-Red Permutation - https://codeforces.com/gym/594356/problem/E

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    colors = input().strip()
    
    blue = []
    red = []
    for i in range(n):
        if colors[i] == 'B':
            blue.append(a[i])
        else:
            red.append(a[i])
            
    blue.sort()
    red.sort(reverse=True)

    valid = True

    for i, x in enumerate(blue): #[1,0]
        if x < i + 1:
            valid = False
            break
        
    for i, x in enumerate(red):#[3,4]
        if x > n - i:
            valid = False
            break

    print("YES" if valid else "NO")