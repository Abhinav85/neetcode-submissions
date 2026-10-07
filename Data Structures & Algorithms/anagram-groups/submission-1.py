class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i, s in enumerate(strs):
            mem = [0] * 26
            for char in s:
                mem[ord(char) - ord('a')] += 1
            if tuple(mem) in ans:
                ans[tuple(mem)].append(s)
            else:
                ans[tuple(mem)] = [s]

        return list(ans.values())


        
        