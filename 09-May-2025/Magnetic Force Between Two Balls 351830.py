# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l,r=1,max(position)
        ans=0
        while l<=r:
            mid=(l+r)//2
            re=position[0]
            c=1
            for i in range(1,len(position)):
                if position[i]-re>=mid:
                    c+=1
                    re=position[i]
                    if c>=m:
                        break
            if c>=m:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans




        return (max(position)-min(position))//(m-1)