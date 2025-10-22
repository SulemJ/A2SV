# Problem: Can Place Flowers - https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans=0
        i=0
        if len(flowerbed) ==1:
            if n==1:
                return flowerbed[0]==0 
            if n==0:
                return True
            else:
                return False
        while i < len(flowerbed):
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    ans+=1
                    i+=2
                else:
                    i+=1
            elif i ==len(flowerbed)-1:
                if flowerbed[i-1]==0 and flowerbed[i]==0:
                    ans+=1
                    i+=2
                else:
                    return True if ans >= n else False
            elif flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                ans+=1
                i+=2
            else:
                i+=1
        return True if ans >= n else False