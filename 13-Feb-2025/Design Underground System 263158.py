# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.travel = {}
        self.avr = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
       self.travel[id]=[stationName, t]

        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        x=self.travel[id]
        if x[0]+"-"+stationName in self.avr:
            T = self.avr[x[0]+"-"+stationName]
            T.append(t-x[1])
            # self.travel.pop(id)
            # return t-x[1]
        else:
            self.avr[x[0]+"-"+stationName]=[t-x[1]]
            # self.travel.pop(id)
            # return t-x[1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if startStation+"-"+endStation in self.avr:
            T = self.avr[startStation+"-"+endStation]
            return sum(T)/len(T)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)