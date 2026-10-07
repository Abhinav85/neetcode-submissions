class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num][0] = freq[num][0] + 1
            else:
                freq[num] = [1,num]
        
        freq_arr = [[] for _ in range(len(nums) + 1)]

        for count, num in list(freq.values()):
            freq_arr[count].append(num)
                
        ans = []
        count = 0
        for i in range(len(freq_arr)-1,-1,-1):
            for num in freq_arr[i]:
                ans.append(num)
            if len(ans) >= k:
                break

        return ans


        

        

        
        