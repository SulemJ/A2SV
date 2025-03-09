# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # d= defaultdict(int)
        d= [(x[0],i) for i,x in enumerate(intervals) ]
        d.sort()
        a=[]
        for x in intervals:
            e=x[1]
            c=-1
            for s,i in d:
                if s >= e:
                    # a.append(i)
                    c=i
                    break
            a.append(c)
        return a
                
       
"""
save the starts and the positions in dict
sort that dict
loop through the end and through the dict and check if start >= end return that j if not -1  

"""        
