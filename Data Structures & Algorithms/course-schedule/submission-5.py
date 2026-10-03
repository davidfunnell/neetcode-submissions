class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        aList = {}

        for i in range(numCourses):
            aList[i] = []

        for crs, pre in prerequisites:
            aList[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if aList[crs] == []:
                return True
            
            visited.add(crs)

            for pre in aList[crs]:
                if dfs(pre) == False:
                    return False

            aList[crs] = []
            visited.remove(crs)

            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False

        return True

        
