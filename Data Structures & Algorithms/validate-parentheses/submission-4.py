class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b_map = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for char in s:
            if char in b_map.values():
                stack.append(char)
            else:
                if len(stack) == 0 or b_map[char] != stack.pop():
                    return False

        if len(stack) > 0:
            return False
        return True

        