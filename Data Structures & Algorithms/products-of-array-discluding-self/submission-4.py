class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult = [1]* (len(nums) + 2)
        suffix_mult = [1] * (len(nums) + 2)

        for i in range(len(nums) + 2):
            if i >= 1 and i <= len(nums):
                prefix_mult[i] = nums[i-1] * prefix_mult[i-1]

        for i in range(len(nums) + 2, -1,-1):
            if i >= 1 and i <= len(nums):
                suffix_mult[i] = nums[i-1] * suffix_mult[i+1]

        ans = [1]* (len(nums))
        for i in range(len(nums) + 1):
            if i >= 1 and i <= len(nums):
                ans[i-1] = prefix_mult[i-1] * suffix_mult[i + 1]
        return ans

        