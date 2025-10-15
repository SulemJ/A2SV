# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a,b),v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1/v

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1
            if start == end:
                return 1.0
            
            visited = set([start])
            pq= deque([(start, 1.0)])

            while pq:
                node, prod= pq.popleft()

                if node == end:
                    return prod

                for nei, val in graph[node].items():
                    if nei not in visited:
                        visited.add(nei)
                        pq.append([nei,val*prod])
            return -1.0

        res=[]
        for a,b in queries:
            res.append(bfs(a,b))
        return res