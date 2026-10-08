class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * ( COLS + 1) for _ in range(ROWS  + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1] = prefix + above


    def sumRegion(self,row1: int,col1: int,row2: int,col2: int) -> int:
        bottom_right = self.sumMat[row2 + 1][col2 + 1]
        top = self.sumMat[row2+1][col1]
        left = self.sumMat[row1][col2 + 1]
        top_left = self.sumMat[row1][col1]
        return bottom_right - top - left + top_left