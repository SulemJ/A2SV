# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.endNode = False

    class Trie:
        def __init__(self):
            self.root = Solution.TrieNode()

        def insert(self, word) -> 'Solution.TrieNode':
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Solution.TrieNode()
                curr = curr.children[c]
            curr.endNode = True
            return curr

    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        trie = self.Trie()
        nodes = {}
        for word in words:
            node = trie.insert(word[::-1])
            nodes[word] = node
        ans = 0
        for word, node in nodes.items():
            if node.endNode and not node.children:
                ans += len(word) + 1
        return ans