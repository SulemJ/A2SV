# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.count += 1

        buckets = defaultdict(list)
        for ch, child in root.children.items():
            buckets[ch].append(child)

        ans = 0

        for ch in s:
            waiting = buckets[ch]
            buckets[ch] = []  

            for node in waiting:
                if node.count > 0:       
                    ans += node.count
                for nxt_ch, nxt_node in node.children.items():
                    buckets[nxt_ch].append(nxt_node)

        return ans