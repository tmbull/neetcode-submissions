class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create adjacency list
        # traverse adjacency list to confirm that there are no cycles
        # while traversing, save the visited nodes 
        prereqs = {i: [] for i in range(numCourses)}
        for [course, req] in prerequisites:
            prereqs[course].append(req)


        visited = set()
        results = {}

        def dfs(crs):
            if crs in visited:
                return False
            
            if not prereqs[crs]:
                results[crs] = None
                return True

            visited.add(crs)

            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            prereqs[crs] = []

            results[crs] = None
            return True
            

        for course in prereqs.keys():
            if not dfs(course):
                return []

        return list(results.keys())

