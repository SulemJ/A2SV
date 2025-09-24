# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            idx= ord(i)-ord('a')
            if idx not in cur.children:
                cur.children[idx] =TrieNode()
            cur=cur.children[idx]
        cur.is_end=True
    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            idx= ord(i)-ord('a')
            if idx not in cur.children:
                return False
                # cur.children[idx] =TrieNode()
            cur=cur.children[idx]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            idx= ord(i)-ord('a')
            if idx not in cur.children:
                return False
                # cur.children[idx] =TrieNode()
            cur=cur.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)