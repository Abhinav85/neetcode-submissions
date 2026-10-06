class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in num_map:
                return [num_map[to_find],i]
            
            num_map[num] = i


