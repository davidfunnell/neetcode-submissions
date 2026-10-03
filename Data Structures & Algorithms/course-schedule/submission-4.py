class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {}

        for i in range(numCourses):
            adjList[i] = []
        
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if adjList[crs] == []:
                return True
            
            visited.add(crs)

            for pre in adjList[crs]:
                if dfs(pre) == False:
                    return False
            
            adjList[crs] = []
            visited.remove(crs)
        
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        
        return True