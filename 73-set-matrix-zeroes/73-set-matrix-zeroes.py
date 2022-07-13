class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, column = len(matrix), len(matrix[0]) 
        var = 1
        for r in range(row):
            for c in range(column):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        var = 0
                    else:
                        matrix[r][0] = 0
        
        print(matrix)
        for r in range(1, row):
            for c in range(1, column):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        print(matrix)
        
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0
                
        if var == 0:
            for c in range(column):
                matrix[0][c] = 0
        return matrix
                    
                    
        