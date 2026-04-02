class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adj list of prerequisites
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        # a course 3 possible state:
        # visited -> crs has been added to output
        # visiting -> crs not added to output, but added o cycle
        # unvisited -> crs not added to output or cycle
        cycle = set()
        visit = set()
        output = []

        def dfs (crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return[]
        
        return output


