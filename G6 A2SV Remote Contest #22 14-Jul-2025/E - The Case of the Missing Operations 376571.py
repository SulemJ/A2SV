# Problem: E - The Case of the Missing Operations - https://codeforces.com/gym/622136/problem/E

import heapq
t=int(input())
heap=[]
res=[]
for _ in range(t):
    op=list(map(str, input().split()))    
    if op[0] == "insert":
        # x=
        res.append("insert " + op[1])
        heapq.heappush(heap, int(op[1]))
    elif op[0] == "removeMin":
        if len(heap) == 0:
            # heapq.heappush(heap, 0)
            res.append("insert 9")
        else:
            heapq.heappop(heap)
        res.append("removeMin")
            # res.append("removeMin")
    elif op[0] == "getMin":
            # if heap:
            # x=
            while len(heap) > 0 and heap[0] < int(op[1]):
                heapq.heappop(heap)
                res.append("removeMin")
            if len(heap) == 0 or heap[0] != int(op[1]):
                heapq.heappush(heap, int(op[1]))
                res.append("insert " + op[1])
            res.append("getMin " + op[1])
print(len(res))
for o in res:
    print(o)