# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        
        conn = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)],
        }
        
        def dfs(x,y):
            if x == m-1 and y == n-1:
                return True
            visited[x][y]=True

            for dx,dy in conn[grid[x][y]]:
                nx,ny=dx+x,dy+y
                if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                    for sx,sy in conn[grid[nx][ny]]:
                        if nx+sx==x and ny+sy==y:
                            if dfs(nx,ny):
                                return True
            return False
        return dfs(0,0)