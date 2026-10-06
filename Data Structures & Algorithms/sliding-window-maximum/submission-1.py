class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res_arr = []
        dq = deque()
        l = 0
        r = 0

        while r < len(nums):
            while dq and dq[-1] < nums[r]:
                dq.pop()
            dq.append(nums[r])

            if r + 1 >= k:
                res_arr.append(dq[0])
                if nums[l] == dq[0]:
                    dq.popleft()
                l = l + 1
            r = r + 1
        return res_arr