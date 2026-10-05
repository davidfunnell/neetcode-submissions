class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = len(matrix) * len(matrix[0])
        rMax = len(matrix)
        cMax = len(matrix[0])

        result = []

        r = 0
        c = 0

        while visited > 0:
            

            while visited > 0 and c+1 < cMax and matrix[r][c+1] != "x":
                result.append(matrix[r][c])
                matrix[r][c] = "x"
                c += 1
                visited -= 1
            while visited > 0 and r+1 < rMax and matrix[r+1][c] != "x":
                result.append(matrix[r][c])
                matrix[r][c] = "x"
                r += 1
                visited -= 1
            while visited > 0 and c-1 >= 0 and matrix[r][c-1] != "x":
                result.append(matrix[r][c])
                matrix[r][c] = "x"
                c -= 1
                visited -= 1
            while visited > 0 and r-1 >= 0 and matrix[r-1][c] != "x":
                result.append(matrix[r][c])
                matrix[r][c] = "x"
                r -= 1
                visited -= 1
            if visited == 1:
                result.append(matrix[r][c])
                break
        return result
