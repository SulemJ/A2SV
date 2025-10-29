# Problem: Get Maximum in Generated Array - https://leetcode.com/problems/get-maximum-in-generated-array/description/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0: return 0
        n+=1
        ans=[0,1]
        for i in range(2,n):
            if i %2==0:
                ans.append(ans[i//2])
            else:
                ans.append(ans[i//2]+ans[(i//2)+1])
        return max(ans)