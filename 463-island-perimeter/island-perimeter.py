class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0:
                return 1
            if grid[r][c] == -1:
                return 0

            grid[r][c] = -1
            
            return (dfs(r + 1, c) + 
                    dfs(r - 1, c) + 
                    dfs(r, c + 1) + 
                    dfs(r, c - 1))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i,j)
        

        