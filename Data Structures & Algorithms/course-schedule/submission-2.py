class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for cur,pre in prerequisites:
            preMap[cur].append(pre)
        
        visited = set()

        def dfs(cur):
            if cur in visited:
                return False
            if preMap[cur]==[]:
                return True
            visited.add(cur)
            for pre in preMap[cur]:
                if not dfs(pre): 
                    return False
            visited.remove(cur)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True