class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = collections.deque()
        fresh = 0
        minutes = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [[1,0],[-1,0], [0,1], [0,-1]]

        while q and fresh > 0:

            for loop in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:

                    if r + dr < 0 or r + dr == m or c + dc < 0 or c + dc == n or grid[r+dr][c+dc] != 1:
                        continue
                    grid[r+dr][c+dc] = 2
                    q.append((r+dr,c+dc))
                    fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1


                

