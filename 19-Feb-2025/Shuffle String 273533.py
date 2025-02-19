# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d= {i:x for i, x in zip(indices,s)}
        d=dict(sorted(d.items()))
        a=[i for x,i in d.items()]
        return "".join(a)