class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen, colLen = len(matrix), len(matrix[0])
        row, col = 0, colLen - 1
        while (row >= 0 and row < rowLen) and (col >=0 and col < colLen):
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False