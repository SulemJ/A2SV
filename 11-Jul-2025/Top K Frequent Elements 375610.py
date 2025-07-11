# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        res=[]
        sor = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
        for i,g in enumerate(sor):
            if i<k:
                res.append(g)
            else:
                break
        # print(res)

        return res