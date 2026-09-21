class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        origin = image[sr][sc]

        if origin == color:
            return image

        def dfs(r,c):

            if r == m or c == n or r < 0 or c < 0 or image[r][c] != origin:
                return


            image[r][c] = color


            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return


        dfs(sr,sc)

        return image