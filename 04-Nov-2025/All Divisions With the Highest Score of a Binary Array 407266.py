# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n=len(nums)
        sumOne = sum(nums)
        sumZero= n-sumOne
        maxScore=max(sumOne,sumZero)

        prefix = []
        st=0
        for i in nums:
            st+=i
            prefix.append(st)
        # post=[]
        # en=0
        # for i in nums[::-1]:
        #     en+=i
        #     post.append(st)
        # post.reverse()
        ans=[sumOne]
        for i in range(n):
            numsofOnes = sumOne - prefix[i]
            numsofZeros = (i+1)- prefix[i]
            ans.append(numsofZeros+numsofOnes)
        ans.append(sumZero)
        mx=max(ans)
        a=[i for i in range(n+1) if ans[i]==mx]
        return a

