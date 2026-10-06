import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for s in tokens:
            print(num_stack)
            if s in ["+","-","/","*"]:
                if (len(num_stack) < 2):
                    raise ValueError("Num stack is not valid")
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                if s == "+":
                    num_stack.append(num2+num1)
                elif s == "-":
                    num_stack.append(num2-num1)
                elif s == "*":
                    num_stack.append(num1*num2)
                elif s == "/":
                    num_stack.append(int(num2/num1))
            else:
                num_stack.append(int(s))
        return num_stack.pop()
        