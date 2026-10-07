class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        for num in nums:
            if num in ans:
                ans[num][0] = ans[num][0] + 1
            else:
                ans[num] = [1,num]
        
        freq_arr = [[] for _ in range(len(nums) + 1)]

        for count, num in list(ans.values()):
            print(count,num)
            freq_arr[count].append(num)
                
        ans = []
        count = 0
        for i in range(len(freq_arr)-1,-1,-1):
            if freq_arr[i] != []:
                for num in freq_arr[i]:
                    ans.append(num)
            if len(ans) >= k:
                break

        return ans


        

        

        
        