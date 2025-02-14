# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.count = defaultdict(int)
        self.se = defaultdict(list)

    def add(self, number: int) -> None:
        if self.count[number] ==0:
            self.count[number]+=1
            self.se[self.count[number]].append(number)
        else:
            self.count[number]+=1
            self.se[self.count[number]-1].remove(number)
            self.se[self.count[number]].append(number)
    def deleteOne(self, number: int) -> None:
        if self.count[number] !=0:
            self.count[number]-=1
            self.se[self.count[number]+1].remove(number)
            self.se[self.count[number]].append(number)

    def hasFrequency(self, frequency: int) -> bool:
        # for i, x in self.count.items():
        if self.se[frequency] != []:
                return True
        return False

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)