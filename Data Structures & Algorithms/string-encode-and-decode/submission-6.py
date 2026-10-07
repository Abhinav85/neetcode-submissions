class Solution:
    def encode(self, strs: list[str]) -> str:
        final_string = ""
        for s in strs:
            final_string += str(len(s)) + "#" + s
        return final_string

    def decode(self, s: str) -> list[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s):
                if s[j] != "#":
                    j = j +1
                else:
                    length = int(s[i:j])
                    start = j + 1
                    end = start + length
                    ans.append(s[start:end])
                    i = end
                    break

        return ans