# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a,b,v in times:
            graph[a].append((b,v))
        
        min_dist = [float('inf')] *(n+1)
        min_dist[k]= 0

        hp=[(k, 0)]

        while hp:
            node, val= heapq.heappop(hp)

            if val > min_dist[node]:
                continue

            for b, v in graph[node]:
                new_val = v+val
                if new_val < min_dist[b]:
                    min_dist[b] = new_val
                    heapq.heappush(hp, (b, new_val))
        
        total_min = max(min_dist[1:])
        return total_min if total_min != float('inf') else -1


      