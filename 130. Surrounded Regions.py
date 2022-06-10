class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # DFS to mark...
        q = deque()
        
        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != 'O':
                return
            
            board[r][c] = "Z"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == "O" and (i in [0, len(board) - 1] or j in [0, len(board[0]) - 1])):
                    dfs(i, j)
                
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Z":
                    board[i][j] = "O"
