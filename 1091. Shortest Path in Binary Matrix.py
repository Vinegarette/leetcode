class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        q.append([0, 0])
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                
                if [r, c] == [ROWS - 1, COLS - 1]:
                    return ans
                
                # BFS 
                directions = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1], [r + 1, c + 1], [r - 1, c - 1], [r + 1, c - 1], [r - 1, c + 1]]
                for x, y in directions:
                    if (x < 0 or x >= ROWS or y < 0 or y >= COLS or grid[x][y] == 1):
                        continue
                    q.append([x, y])
                    grid[x][y] = 1
        return -1
