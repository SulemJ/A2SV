# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, t: int, m: int) -> int:
       # 10 5 4 2
        ans=0
        while t>1:
            if t==2:
                t-=1
                ans+=1
            elif t %2==0 and m>0:
                t/=2
                m-=1
                ans+=1
            elif t %2!=0 and m>0:
                t-=1
                ans+=1
            else:
                ans+=(t-1)
                t=0
        return int(ans)


        

