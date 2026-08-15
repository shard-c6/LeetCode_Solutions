class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        closed_island_count = 0
        def dfs(r,c):#ye dfs hame valid islands hai ya nahi vo batata hai
            #agar vo boundery out of bounds hai to valid island nahi hai
            if (r<0 or c<0 or r>=rows or c >= cols):
                return False # nahi hai fir valid
            #agar abhi jis tile pr khade hai and vo out of bounds nahi hai aur agar water hai to safe  rhega uske niche upar left right wla land valid hai
            if grid[r][c] == 1:
                return True

            #is wale tile ko visited mark karenge abhi that is 1 (sinking the tile in water) 
            grid[r][c] = 1
            
            right = dfs(r,c+1)
            left = dfs(r,c-1)
            up = dfs(r+1,c)
            down =dfs(r-1,c)

            #abhi check karenge ye tile ke up down left right valid tiles hai ki nahi 
            return (up and down and left and right)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:#agar land hai to dfs maro
                    if dfs(i,j):#agar valid island nikla to count updte kardo
                        closed_island_count+=1
        return closed_island_count

