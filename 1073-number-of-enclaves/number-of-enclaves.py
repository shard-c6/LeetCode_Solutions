class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # 1. Standard, basic DFS. No booleans, no counting. Just sink!
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return
            
            grid[r][c] = 0
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 2. Walk the borders and trigger DFS to sink invalid islands
        for i in range(rows):
            for j in range(cols):
                # Is this cell exactly on the border?
                if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                    # If it's land on the border, sink it and all connected land!
                    if grid[i][j] == 1:
                        dfs(i, j)

        # 3. All invalid islands are gone. Now just count what's left!
        total_enclaves = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    total_enclaves += 1

        return total_enclaves