class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        visited = {(0, 0)}
        queue = deque([(0, 0)])
        length = 1

        neighbors = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1],          [0, 1],
            [1, -1],  [1, 0], [1, 1]
        ]

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == n - 1 and c == n - 1:
                    return length

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc

                    if (
                        nr < 0 or nr >= n
                        or nc < 0 or nc >= n
                        or (nr, nc) in visited
                        or grid[nr][nc] == 1
                    ):
                        continue

                    queue.append((nr, nc))
                    visited.add((nr, nc))

            length += 1  # Finished this level; move to the next distance.

        return -1