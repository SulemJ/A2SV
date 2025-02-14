# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        exc=[]
        for i, x in count.items():
            if i == 0:
                exc.append(x)
            else:
                if x%(i+1)!=0 :                   
                    exc.append(((x//(i+1))*(i+1) + (i+1)))
                elif x%(i+1)==0:
                    exc.append(((x//(i+1))*(i+1)))
        return sum(exc)