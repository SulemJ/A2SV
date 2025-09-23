# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True
    
    def getLongestCommonPrefix(self) -> str:
        node = self.root
        prefix = []
        
        while node:
            if len(node.children) != 1 or node.isEnd:
                break
            ch = next(iter(node.children))
            prefix.append(ch)
            node = node.children[ch]
        
        return "".join(prefix)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        trie = Trie()
        for word in strs:
            trie.insert(word)
        
        return trie.getLongestCommonPrefix()
