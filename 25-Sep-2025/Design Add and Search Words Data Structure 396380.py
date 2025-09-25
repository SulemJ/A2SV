# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            idx= ord(i)-ord('a')
            if idx not in cur.children:
                cur.children[idx] =TrieNode()
            cur=cur.children[idx]
        cur.is_end=True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            cur=node
            for i in range(j, len(word)):
                char = word[i]
                if char =='.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    # cur = self.root
                    # for i in word:
                    idx= ord(char)-ord('a')
                    if idx not in cur.children:
                        return False
                            # cur.children[idx] =TrieNode()
                    cur=cur.children[idx] 
            return cur.is_end
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)