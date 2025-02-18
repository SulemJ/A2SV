# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obsSet = set(map(tuple, obstacles))
        # directions = [0, 1, 2, 3]  # 0: north, 1: east, 2: south, 3: west
        x = y = dir = 0
        maxDist = 0
        
        for cmd in commands:
            if cmd == -1:
                dir = (dir + 1) % 4
            elif cmd == -2:
                dir = (dir + 3) % 4
            else:
                for _ in range(cmd):
                    newX = x + (dir == 1) - (dir == 3)
                    newY = y + (dir == 0) - (dir == 2)
                    if (newX, newY) not in obsSet:
                        x, y = newX, newY
                    else:
                        break
            maxDist = max(maxDist, x * x + y * y)       
        return maxDist