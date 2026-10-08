class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            if num <= 0 or num > len(nums):
                nums[i] = len(nums) + 2
        
        for i, num in enumerate(nums):
            val = abs(num)
            if 1 <= val <= len(nums):
                idx = val - 1
                nums[idx] = -abs(nums[idx])
                
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1
        