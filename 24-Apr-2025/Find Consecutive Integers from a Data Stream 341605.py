# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        # self.a=deque()
        # self.ch=True
        self.cnt=0
    def consec(self, num: int) -> bool:
        # if self.cnt==self.k:
        #     s=self.a.popleft()
        #     if s ==self.value:

            # self.cnt-=1
        # self.a.append(num)
        # self.cnt+=1
        if num!=self.value:
            self.cnt=0
        else:
            self.cnt+=1
   
        if self.cnt>=self.k:
            return True
        else:
            return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)