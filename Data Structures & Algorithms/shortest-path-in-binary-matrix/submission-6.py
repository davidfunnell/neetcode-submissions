class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        length = 0
        q = deque([(0,0,1)]) #r,c,length


        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        visited = set()

        while q:

            r, c, length = q.popleft()

            visited.add((r,c))

            if r == n-1 and c == n-1:
                return length


            for dr, dc in directions:
                row = r + dr
                col = c + dc

                if (0 <= row < n and 0 <= col < n) and (row,col) not in visited and grid[row][col] == 0:
                    q.append((row,col, length + 1))


        return -1



