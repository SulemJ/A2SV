# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def isPrerequisite(self, graph: dict, visited: List[bool], src: int, target: int
    ) -> bool:
            # visited =[]
        visited[src] =True
        if src == target:
            return True
        for neigh in graph.get(src,[]):
            if not visited[neigh]:
                if self.isPrerequisite(graph, visited,neigh, target):
                    return True
        return False
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i: [] for i in range(numCourses)}

        for neigh in prerequisites:
            graph[neigh[0]].append(neigh[1])
        
        res=[]

        for query in queries:
            visited = [False] * numCourses

            res.append(self.isPrerequisite(graph, visited, query[0], query[1]))
        return res