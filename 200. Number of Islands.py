class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Its good tho 
        
    
        ROWS = len(grid)
        COLS = len(grid[0])
        
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            directions = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for direction in directions:
                dfs(direction[0], direction[1])
        
        
        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r, c)
                    
        return ans
