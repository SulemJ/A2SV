# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, n: List[int], t: int) -> int:
        """
        i,j=0
        """
        c=0
        n.sort()
        for i in range(len(n)-1):
            j=len(n)-1
            while i<j:
                if n[i]+n[j]<t:
                    c+=1
                    j-=1
                else:
                    j-=1
        return c

        
        
        
        # l,r=0,len(n)-1
        # while l<r:
        #     su=n[l]+n[r]
        #     if su<t:
        #         l+=1
        #         c+=1
        #     elif su>t:
        #         r-=1
        #     else:
        #         # c+=1
        #         l+=1
        #         r-=1
        # return c