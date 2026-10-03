class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []


        # 0 :
        # 1 : 0
        # 2 : 

        aList = {}
        for i in range(numCourses):
            aList[i] = []
        
        for c, p in prerequisites:
            aList[c].append(p)
        
        visited = set()
        added = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if crs in added:
                return True
            
            visited.add(crs)
            for pre in aList[crs]:
                if dfs(pre) == False:
                    return False
            
            visited.remove(crs)
            added.add(crs)
            result.append(crs)

            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []


        return result
