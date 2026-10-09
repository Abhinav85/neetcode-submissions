class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        tf = 1
        while r < len(nums):
            if nums[l] == nums[r]:
                r = r + 1
            else:
                nums[tf] = nums[r]
                r = r + 1
                tf = tf + 1
                l = l + 1
        return l + 1
        