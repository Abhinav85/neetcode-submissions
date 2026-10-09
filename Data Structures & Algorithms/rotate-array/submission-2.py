class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k == 0:
            return nums

        rotate_factor = k%n

        if rotate_factor == 0:
            return nums
        
        def reverse(l,r):
            while l<= r:
                nums[l], nums[r] = nums[r], nums[l]
                l = l + 1
                r = r - 1
        
        reverse(0,n-1)
        reverse(0,rotate_factor-1)
        reverse(rotate_factor,n-1)

        return nums




