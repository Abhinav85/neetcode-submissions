class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checker = {}
        ans = True
        def box_num(i,j):
           return "b" + str((i//3)*3) + str(j//3)

        def checkLogic(key, char):
            values = checker.setdefault(key, set())

            if char in values:
                return False

            values.add(char)
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
        print(checker)

        return ans


