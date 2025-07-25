# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        queue = deque()
        for i in range(m):
            for j in (0, n - 1):
                if board[i][j] == 'O':
                    queue.append((i, j))
        for j in range(n):
            for i in (0, m - 1):
                if board[i][j] == 'O':
                    queue.append((i, j))
    
        while queue:
            i, j = queue.popleft()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    queue.append((i + di, j + dj))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'