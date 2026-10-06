class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if num in num_map:
                num_map[num].append(i)
            else:
                num_map[num] = [i]

        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in num_map:
                if num_map[to_find][0] == i:
                    if len(num_map[to_find]) == 1:
                        continue
                    else:
                        return [i,num_map[to_find][1]]
                return [i,num_map[to_find][0]]
