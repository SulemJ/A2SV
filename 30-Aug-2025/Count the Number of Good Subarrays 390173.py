# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = ans = c = 0
        n, d = len(nums), defaultdict(int)
        for i,x in enumerate(nums):   
            c += d[x]
            d[x] += 1

            while c >= k:              
                ans+= n - i
                d[nums[l]] -= 1           
                c -= d[nums[l]]
                l += 1
            
        return ans     