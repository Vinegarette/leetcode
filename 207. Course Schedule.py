class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mp = collections.defaultdict(list)
        # Generate all prereqs for each 
        
        for a, b in prerequisites:
            mp[a].append(b)
        
        # Standard DFS, return if no prereqs
        # Remove prereqs as they are validated
        def dfs(course, visited):
            toVisit = mp[course]
            if (len(toVisit) == 0):
                return True
            
            if course in visited:
                return False
            
            visited.add(course)
            
            for prereq in toVisit:
                if dfs(prereq, visited) == False:
                    return False
                mp[course].remove(prereq)
            
            return True
            
            
            
        # Run thru dfs
        for course in range(numCourses):
            visited = set()
            if (dfs(course, visited) == False):
                return False
            
        return True
