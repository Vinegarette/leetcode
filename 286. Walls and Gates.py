class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS = len(rooms)
        COLS = len(rooms[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if(rooms[r][c] == 0):
                    q.append([r, c])
        dist = 0     
        while q:
            dist += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                temp = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
                for r2, c2 in temp:
                    if (r2 < 0 or c2 < 0 or r2 == ROWS or c2 == COLS or rooms[r2][c2]==-1):
                        continue
                    if dist < rooms[r2][c2]:
                        rooms[r2][c2] = dist
                        q.append([r2, c2])
                
                
            
