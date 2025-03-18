# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        i,j=0,len(n)-1
        while i<j:
            if n[i]+n[j]<t:
                i+=1
            elif n[i]+n[j]>t:
                j-=1
            else:
                return [i+1,j+1]