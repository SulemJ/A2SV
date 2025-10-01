# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        ans=[]
        check=set()
        cur=s[0]
        i=0
        while i<len(s):
            if cur not in check:
                ans.append(cur)
                check.add(cur)
                if i<len(s)-1:
                    i+=1
                    cur= s[i]
                else:
                    break
            elif cur in check and i<len(s)-1:
                i+=1
                cur+=s[i]
            else:
                break
        return ans
