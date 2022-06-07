class Solution:
    # General idea is a hashmap, storing the complement of the number as the Key and index as the value
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i, num in enumerate(nums):
            if num in d:
                return[d[num], i]
            else:
                complement = target - num
                d[complement] = i
        
        return []
