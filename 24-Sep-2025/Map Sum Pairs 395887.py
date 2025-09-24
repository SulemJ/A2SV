# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.total = 0
        self.children = {}

class MapSum:

    def __init__(self):
        self.root=TrieNode()
        self.map={}
    def insert(self, key: str, val: int) -> None:
        dif= val - self.map.get(key,0)
        self.map[key]=val
        cur =self.root
        for i in key:
            idx = ord(i) - ord('a')
            if idx not in cur.children:
                cur.children[idx]= TrieNode()
            cur=cur.children[idx]
            cur.total+=dif
    def sum(self, prefix: str) -> int:
        cur =self.root
        for i in prefix:
            idx = ord(i) - ord('a')
            if idx not in cur.children:
                # cur.children[idx]= TrieNode()
                return 0
            cur=cur.children[idx]
        return cur.total


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)