class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preDict = { i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preDict[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if preDict[crs] == []:
                return True
            
            visited.add(crs)

            for pre in preDict[crs]:
                if dfs(pre) == False:
                    return False
            
            visited.remove(crs)
            preDict[crs] = []
            return True



        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False

        return True