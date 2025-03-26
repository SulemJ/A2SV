# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        Cw=0
        for i in range(0, k):
            if blocks[i]=='W':
                Cw+=1
                
        c=Cw
        for i in range(k, n):
            if blocks[i-k]=='W':
                Cw-=1
            if blocks[i]=='W':
                Cw+=1
            c=Cw if Cw<c else c
        
        return c

