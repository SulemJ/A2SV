# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c=defaultdict(int)
        for i in range(len(arr)):
            c[arr[i]%k]+=1
        for i,x in c.items():
            if i!= 0 and c[k-i] != x:
                return False
            elif i==0 and x%2==1:
                return False

        return True




        #     arr[i]=arr[i]%k
        #     if arr[i]%k==0:
        #         arr[c], arr[i]= arr[i], arr[c]
        #         c+=1
        # if c%2:
        #     return False
        # s=c
        # arr[c:] = sorted(arr[c:])
        # e = len(arr)-1
        # while s < e:
        #     if (arr[s]+arr[e])%k:
        #         return False
        #     s+=1
        #     e-=1
        # return True



