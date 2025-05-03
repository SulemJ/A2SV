# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.s=[]
        self.ind=0
    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        x=self.s[self.ind]
        self.ind+=1
        
        return x

    def peek(self) -> int:
        return self.s[self.ind]

    def empty(self) -> bool:
        return (len(self.s)-self.ind)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()