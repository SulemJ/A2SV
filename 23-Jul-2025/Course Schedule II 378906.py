# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        order=[]

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course]+=1

        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            order.append(course)

            for nei in graph[course]:
                incoming[nei]-=1
                if incoming[nei] == 0:
                    queue.append(nei)
        if len(order) != numCourses:
            return []
        return order    