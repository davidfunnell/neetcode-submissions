class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsDict = { i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            crsDict[crs].append(pre)

        cycle = set()
        visited = set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            
            cycle.add(crs)

            for pre in crsDict[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            output.append(crs)
            visited.add(crs)
            return True

        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []

        return output