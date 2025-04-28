# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        c=0
        for i in range(len(t)):
            if i<=k:
                c+=(t[k] if t[k]<t[i] else t[i])
            else:
                c+=(t[k]-1 if (t[k]-1)<t[i] else t[i])

        return c