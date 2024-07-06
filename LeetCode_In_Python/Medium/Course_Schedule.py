class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        def course_schedule(numCourses, prerequisites):
            prerequisite_dict = {}
            for prerequisite, course in prerequisites:
                if course in prerequisite_dict:
                    prerequisite_dict[course].append(prerequisite)
                else:
                    prerequisite_dict[course] = [prerequisite]
            done = set()
            for course in prerequisite_dict:
                if course not in done:
                    discovered = set()
                    discovered.add(course)
                    if detect_cycle(course, prerequisite_dict, discovered, done):
                        return False
            return True




        def detect_cycle(course,prerequisite_dict,discovered, done):
            if course in prerequisite_dict and course not in done:
                for prerequisite in prerequisite_dict[course]:
                    if prerequisite in discovered:
                        return True
                    discovered.add(prerequisite)
                    is_cycle = detect_cycle(prerequisite, prerequisite_dict, discovered,done)
                    if is_cycle:
                        return True
            discovered.remove(course)
            done.add(course)
            return False
        return course_schedule(numCourses, prerequisites)