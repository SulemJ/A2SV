# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        c = []
        res = [0]*len(score)
        for i in range(len(score)):
            c.append([score[i],i+1])
        c.sort(reverse=True)
        for j in range(len(c)):
            if j== 0:
                res[c[j][1]-1] ="Gold Medal"
            elif j== 1:
                res[c[j][1]-1] ="Silver Medal"
            elif j== 2:
                res[c[j][1]-1] ="Bronze Medal"
            else:
                res[c[j][1]-1] =f"{j+1}"
        return res