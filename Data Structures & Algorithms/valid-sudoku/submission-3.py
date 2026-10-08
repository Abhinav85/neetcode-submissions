class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checker = {}
        ans = True
        def box_num(i,j):
            if i < 3:
                if j < 3:
                    return "b1"
                elif j >2 and j < 6:
                    return "b2"
                else:
                    return "b3"
            elif i > 2 and i < 6:
                if j < 3:
                    return "b4"
                elif j >2 and j < 6:
                    return "b5"
                else:
                    return "b6"
            else:
                if j < 3:
                    return "b7"
                elif j >2 and j < 6:
                    return "b8"
                else:
                    return "b9"

        def checkLogic(key,char):
            if key in checker:
                if char in checker[key]:
                    return False
                else:
                    checker[key].append(char)
            else:
                checker[key] = [char]
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                if char != ".":
                    key_i = "R" + str(i)
                    key_j = "C" + str(j)
                    key_box = box_num(i,j)
                    if not(checkLogic(key_i, char) and checkLogic(key_j, char) and checkLogic(key_box,char)):
                        ans = False

        return ans


