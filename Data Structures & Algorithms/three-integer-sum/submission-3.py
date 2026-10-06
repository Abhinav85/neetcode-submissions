class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num = -1 * nums[i]
            r = len(nums) - 1
            l = i + 1

            while r > l:
                num1 = nums[l]
                num2 = nums[r]
                if num1 + num2 > num:
                    r = r - 1
                elif num1 + num2 < num:
                    l = l + 1
                else:
                    print(num, num1, num2)
                    res.append([-1*num, num1, num2])
                    r = r - 1
                    l = l + 1
                    while nums[l] == nums[l-1] and l  < r:
                        l = l + 1

        return res

        