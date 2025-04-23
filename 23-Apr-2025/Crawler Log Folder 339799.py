# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        a=0
        for i in logs:
            if i == "../":
                if a>0:
                    a-=1
                else:
                    continue
            elif i == './':
                continue
            else:
                a+=1
        return a