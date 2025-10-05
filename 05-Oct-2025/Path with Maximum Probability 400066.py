# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (a,b), prob in zip(edges,succProb):
            graph[a].append((b,prob))
            graph[b].append((a,prob))
        
        max_prob=[0.0] * n
        max_prob[start_node] = 1.0

        hp=[(-1.0,start_node)]

        while hp:
            cur_prob, node =  heapq.heappop(hp)
            cur_prob = -cur_prob

            if node == end_node:
                return cur_prob
            
            for neigh, prob in graph[node]:
                new_prob = prob * cur_prob
                if new_prob > max_prob[neigh]:
                    max_prob[neigh] = new_prob
                    heapq.heappush(hp, (-new_prob, neigh))

        return 0.0