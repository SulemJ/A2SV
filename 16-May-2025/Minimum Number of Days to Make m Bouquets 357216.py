# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        ans=-1
        l,r=0, max(bloomDay)
        while l<=r:
            mid=(l+r)//2
            s,c=0,0
            for i in bloomDay:
                # if s==k:
                #     c+=1
                #     s=0
                if mid >= i:
                    s+=1
                    if s>=k:
                        s=0
                        c+=1
                else:
                    s=0
            if c>=m:
                ans=mid
                r=mid-1
            else:
                l=mid+1
            # else:
            #     return mid

        return ans


