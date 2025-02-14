# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color =defaultdict(int)
        colors ={}
        n =limit+1
        arr=[]
        for i ,x in queries:
            if i <= n:
                if color[i] == 0 and x not in colors:
                    color[i]=x
                    colors[x]=[i] #color {1:4,}{1:4,2:5}{1:3,2:5}{1:3, 2:5, 3:4}
                    #colors{4:[1]}{4:[1], 5:[2]}{4:[0],5:[2],3:[1] }{4:[1]}
                elif color[i] == 0 and x  in colors:
                    color[i]=x
                    colors[x].append(i)
                elif color[i] != 0 and x not in colors:
                    y = color[i]
                    colors[y].remove(i)
                    if colors[y] == []:           
                        colors.pop(y)
                    color[i]=x
                    colors[x]=[i]
                elif color[i] != 0 and x  in colors:
                    y = color[i]
                    colors[y].remove(i)
                    if colors[y] == []:           
                        colors.pop(y)
                    color[i]=x
                    if x in colors:
                        colors[x].append(i)
                    else:
                        colors[x]=[i]
                    
                arr.append(len(colors))

        
        return arr









