class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        maxArea = 0

        def dfs(r, c, area):
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == 0:
                return area

            grid[r][c] = 0
            area += 1

            area = dfs(r+1, c, area)
            area = dfs(r-1, c, area)
            area = dfs(r, c+1, area)
            area = dfs(r, c-1, area)

            return area

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    area = 0
                    area = dfs(r, c, area)
                    maxArea = max(maxArea, area)

        return maxArea