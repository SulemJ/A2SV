# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        adj = defaultdict(set)
        n = len(s)
        for i, j in pairs:
            adj[i].add(j)
            adj[j].add(i)
        s = list(s)
        seen = set()
        for start in range(n):
            if start in seen:
                continue
            stack = [start]
            comp = set([start])
            while stack:
                cur = stack.pop()
                for nei in adj[cur]:
                    if nei not in comp:
                        comp.add(nei)
                        stack.append(nei)
            seen |= comp
            comp = sorted(comp)
            replace_with = [s[i] for i in sorted(comp, key=lambda i: s[i])]
            for i in range(len(comp)):
                index = comp[i]
                s[index] = replace_with[i]
        return ''.join(s)