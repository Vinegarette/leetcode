class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for num in nums:
            if num in mp:
                return True
            else:
                mp[num] = 1
        return False
        # Troll solution...
        # return True if len(set(nums)) < len(nums) else False
