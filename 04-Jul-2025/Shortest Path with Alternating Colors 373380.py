# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)
        
        for u, v in redEdges:
            red_adj[u].append(v)
        for u, v in blueEdges:
            blue_adj[u].append(v)

        res = [-1] * n
        visited = set()

        q = deque()
        q.append((0, 0, 0))  
        q.append((0, 1, 0))  

        while q:
            node, color, dist = q.popleft()
            
            if (node, color) in visited:
                continue
            visited.add((node, color))

           
            if res[node] == -1:
                res[node] = dist
            else:
                res[node] = min(res[node], dist)

            if color == 0:
                for nei in blue_adj[node]:
                    q.append((nei, 1, dist + 1))
            else:
                for nei in red_adj[node]:
                    q.append((nei, 0, dist + 1))

        return res
