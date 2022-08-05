class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []
        
        def dfs(r, c, visited, prevHeight):
            if (r, c) not in visited:
                if ((r,c) in visited or
                    r not in range(rows) or c not in range(cols) or
                        heights[r][c] < prevHeight):
                    return
                
                visited.add((r,c))
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    dfs(row, col, visited, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
            
        
        