# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        processorTime.sort()
        tasks.sort(reverse=True)
        d=defaultdict(list)
        for i in range(len(processorTime)):
            d[processorTime[i]].append(tasks[((i*4)) :((i+1)*4)])
        a=0
        for i,x in d.items():
            # x=*x
            for j in x[0]:
                a = max(a, i+j )
        return a