# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for a,b,w in zip(original, changed, cost):
            graph[a].append((b,w))
        best = [[float('inf')] * 26 for _ in range(26)]
        for i, x in enumerate(string.ascii_lowercase):
            hp = [(0, x)]
            while hp:
                cost, cur = heapq.heappop(hp)
                if cost >= best[i][ord(cur)- ord('a')]:
                    continue
                best[i][ord(cur) - ord('a')] = cost
                for ns, ncost in graph[cur]:
                    if cost + ncost < best[i][ord(ns)- ord('a')]:
                        heapq.heappush(hp, (cost+ncost, ns))
        
        res = 0
        for i,x in enumerate(source):
            cst= best[ord(x) - ord('a')][ord(target[i]) - ord('a')]
            if cst == float('inf'):
                return -1
            res += cst
        return res


