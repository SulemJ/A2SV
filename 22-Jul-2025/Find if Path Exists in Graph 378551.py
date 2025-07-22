# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited=set()
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for nextnode in graph[node]:
                if nextnode not in visited:
                    if dfs(nextnode):
                        return True

            return False
        return dfs(source)    