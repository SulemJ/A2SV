# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0]>target or letters[-1]<=target:
            return letters[0]   

        l,r=0,len(letters)-1
        while l<=r:
            m=(l+r)//2
            if letters[m]<=target:
                l=m+1
            else:
                r=m-1
        return letters[l]   