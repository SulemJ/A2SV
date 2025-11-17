# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c=Counter(s)
        ans=[]
        i=0
        debt=0
        for j in range(len(s)): #debt=4-1+3-1-1-1+2-1-1-1-1
            if s[j] not in s[i:j]:
                debt+=c[s[j]]
            debt-=1
            if debt==0:
                ans.append(j-i+1)
                i=j+1
        return ans