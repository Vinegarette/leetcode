class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Cycle detection
        # Two pointers, i.e. two robots.
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        x = 0
        y = 0
        direction = 0
        for c in instructions:
            if c == "L":
                direction -= 1
            elif c == "R":
                direction += 1
            else:
                x += directions[direction][0]
                y += directions[direction][1]
            
            if direction < 0:
                direction = 3
            elif direction > 3:
                direction = 0
                
        return x == 0 and y == 0 or direction != 0
