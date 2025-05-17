# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.array=[]

    def book(self, start: int, end: int) -> bool:
        for s,e in self.array:
            if e>start and end>s:
                return False
        self.array.append([start,end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)