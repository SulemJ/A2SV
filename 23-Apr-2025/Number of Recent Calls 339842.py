# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.queue=deque()
        # self.cnt=0
    def ping(self, t: int) -> int:
        self.queue.append(t)
        # self.cnt+=1
        while self.queue and self.queue[0]<t-3000:
                self.queue.popleft()
                # self.cnt-=1
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)