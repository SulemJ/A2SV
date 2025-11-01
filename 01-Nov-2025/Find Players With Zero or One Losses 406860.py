# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w= Counter(matches[i][0] for i in range(len(matches)))
        l= Counter(matches[i][1] for i in range(len(matches)))
        answer =[]
        lostnev=[]
        lostone=[]
        for i,x in l.items():
            if x==1:
                lostone.append(i)
        for w,x in w.items():
            if w not in l:
                lostnev.append(w)
        answer.append(sorted(lostnev))
        answer.append(sorted(lostone))
        return answer
