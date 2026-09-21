class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_count = [0] * numCourses
        next_courses = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            prereq_count[course] += 1
            next_courses[pre].append(course)

        queue = []

        for course in range(numCourses):
            if prereq_count[course] == 0:
                queue.append(course)

        index = 0
        completed = 0

        while index < len(queue):
            course = queue[index]
            index += 1
            completed += 1

            for next_course in next_courses[course]:
                prereq_count[next_course] -= 1

                if prereq_count[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses