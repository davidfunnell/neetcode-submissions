class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        result = 0     

        def dfs(r,c):

            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == "0":
                return
            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    dfs(x,y)
                    result += 1



        return result