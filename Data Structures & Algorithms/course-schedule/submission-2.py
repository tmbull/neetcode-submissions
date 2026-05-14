class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # basic approach:
        # build an adjacency list of course -> prereq
        # do BFS over adjacency list to determine if it is possible
        # to visit all nodes in the graph

        courseMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courseMap[course].append(prereq)

        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if not courseMap[crs]:
                return True

            visited.add(crs)

            for pre in courseMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            courseMap[crs] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
