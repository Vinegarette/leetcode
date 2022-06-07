class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // Hashmap idea
        unordered_map<int, int> hashmap;
        vector<int> result;
        for (int i = 0; i < nums.size(); i ++) {
            // Select a number
            int goal = target - nums[i];
            // If goal is in nums,
            // Return both
            if (hashmap.find(goal) != hashmap.end()) {
                result.push_back(hashmap[goal]);
			    result.push_back(i);
                return result;
            }
        
            
            // Not found, put into hashmap
            hashmap[nums[i]] = i;
            
            
            
        }
        return result;
    }
};
