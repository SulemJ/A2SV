# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.start=[]
        self.past=0
    def ping(self, t: int) -> int:
        self.start.append(t)
        # c=0
        # for i in self.start:
        while self.start[self.past]<t-3000:
                self.past+=1 

        return len(self.start)-self.past


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)