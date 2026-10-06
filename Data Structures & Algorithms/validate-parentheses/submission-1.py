class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposite = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for char in s:
            print(stack)
            if char in opposite.keys():
                stack.append(opposite[char])
            elif char in opposite.values():
                if(len(stack) == 0):
                    return False

                last_char = stack.pop()
                if last_char != char:
                    return False
        
        if len(stack):
            return False
        
        return True

        