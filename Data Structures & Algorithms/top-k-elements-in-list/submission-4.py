class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        temp_arr = [[] for _ in range(len(nums))]
        
        for num, freq in freq_map.items():
            print(num,freq)
            temp_arr[freq-1].append(num)

        res = []
        for i in range(len(temp_arr)-1,-1,-1):
            arr = temp_arr[i]
            if arr == []:
                continue
            for dig in arr:
                res.append(dig)
                if len(res) == k:
                    return res

        return res

        