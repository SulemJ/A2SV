# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(src):
            dist = [float('inf')] * n
            dist[src] = 0
            pq = [(0, src)]
            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                for nei, w in graph[node]:
                    nd = d + w
                    if nd < dist[nei] and nd <= distanceThreshold:
                        dist[nei] = nd
                        heapq.heappush(pq, (nd, nei))
            return dist

        answer = -1
        min_count = float('inf')
        for i in range(n):
            dist = dijkstra(i)
            cnt = sum(1 for j in range(n) if j != i and dist[j] <= distanceThreshold)
            if cnt < min_count or (cnt == min_count and i > answer):
                min_count = cnt
                answer = i

        return answer
