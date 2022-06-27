class Solution {
public:
    bool isRobotBounded(string instructions) {
        vector<vector<int>> directions{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int x = 0;
        int y = 0;
        int direction = 0;
        
        for (char c: instructions) {
            if (c == 'L') {
                direction = (direction + 3) % 4;
            } else if (c == 'R') {
                direction = (direction + 1) % 4;
            } else {
                x += directions[direction][0];
                y += directions[direction][1];
            }
        }
        
        return x == 0 && y == 0 || direction != 0;
    }
};
