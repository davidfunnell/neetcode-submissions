class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        q = deque([(0,0,1)])

        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        visited = set((0,0))

        while q:
            r, c, length = q.popleft()

            if r == n - 1 and c == n - 1:
                return length

            for dr, dc in directions:
                if (0 <= (r + dr) < n and 0 <= (c + dc) < n) and grid[r+dr][c+dc] == 0 and (r+dr,c+dc) not in visited:
                    q.append((r+dr,c+dc,length + 1))
                    visited.add((r + dr,c + dc))

            
        
        return -1
