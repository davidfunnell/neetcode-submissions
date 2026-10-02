class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        
        def dfs(m,n):
            grid[m][n] = "0"


            if m + 1 < rows and grid[m+1][n] ==  "1" :
                dfs(m+1,n)
            if m - 1 >= 0 and grid[m-1][n] == "1":
                dfs(m-1,n)
            if n + 1 < cols and grid[m][n+1] == "1":
                dfs(m,n+1)
            if n - 1 >= 0 and grid[m][n-1] == "1":
                dfs(m,n-1)
            
            return


        for m in range(len(grid)):
            for n in range(len(grid[0])):

                if(grid[m][n]) == "1":
                    dfs(m,n)
                    islands += 1
        

        return islands