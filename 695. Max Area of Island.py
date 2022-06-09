class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Scan thru the entire grid
        # Execute dfs when reaching an island, keeping track of size
        # Turn island into 0s when traversing
        # Return max size
        
        
        
        maxSize = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(r, c, count):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0):
                return count
            
            count += 1
            grid[r][c] = 0
            directions = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for i, j in directions:
                count = dfs(i, j, count)
            
            return count
            
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count = 0
                    maxSize = max(maxSize, dfs(r, c, count))
                    
                    
                    
                    
        return maxSize
