class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # how many 1s?
        fresh = 0
        time = 0

        # BFS
        # deque r, c, times?
        q = deque([])

        # for loop to find all the 2s and add them to the q, sum all the 1s
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c,0))
        
        directions = [[-1,0],[1,0], [0,1], [0,-1]]


        # while q?
        while q:

            r, c, time = q.popleft()

            for dr, dc in directions:
                x = dr + r
                y = dc + c
                if (0 <= x < len(grid) and 0 <= y < len(grid[0])) and grid[x][y] == 1:
                    grid[x][y] = 2
                    q.append((x,y,time + 1))
                    fresh -= 1
        # check up, down, left right
        # update 1 to 2 in grid
        # update 1 variables
        # add freshly updated index to q, increase time by 1

        if fresh > 0:
            return -1
        
        return time


        # if 1 > 0 return -1 else return time




