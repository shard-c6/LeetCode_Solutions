class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>= cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return (1 + dfs(r+1,c)+ dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        current_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    current_area = dfs(i,j)
                    max_area = max(max_area, current_area)
        return (max_area)