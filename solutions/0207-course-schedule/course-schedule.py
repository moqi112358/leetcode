# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
#  
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
#
#
# Example 2:
#
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
#
#
#  
# Constraints:
#
#
# 	The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# 	You may assume that there are no duplicate edges in the input prerequisites.
# 	1 <= numCourses <= 10^5
#
#


class Solution:
    # DFS
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = [[] for _ in range(numCourses)]
        for item in prerequisites:
            pre[item[0]].append(item[1])
        visited = [0] * numCourses
        for node in range(numCourses):
            if not self.dfs(visited, pre, node):
                return False
        return True
    
    def dfs(self, visited, pre, node):
        if visited[node] == -1:
            return False
        if visited[node] == 1:
            return True
        visited[node] = -1
        for i in pre[node]:
            if not self.dfs(visited, pre, i):
                return False
        visited[node] = 1
        return True

# Kahn's algorithm
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         repre = [set() for _ in range(numCourses)] # repre[i] - the next to course i
#         pre = [set() for _ in range(numCourses)] # pre[i] - the previous to course i
#         res = [] # Empty list that will contain the sorted elements
#         graph = set()
#         start = set([i for i in range(numCourses)]) # Set of all nodes with no incoming edge
#         for item in prerequisites:
#             pre[item[0]].add(item[1])
#             repre[item[1]].add(item[0])
#             if item[0] in start:
#                 start.remove(item[0])
#             graph.add((item[1], item[0]))
#         while len(start) != 0:
#             node = list(start)[0]
#             start.remove(node)
#             res.append(node)
#             for nxt_node in repre[node]:
#                 graph.remove((node, nxt_node))
#                 pre[nxt_node].remove(node)
#                 if len(pre[nxt_node]) == 0:
#                     start.add(nxt_node)
        
#         if len(graph) > 0:
#             return False
#         else:
#             return True
                
            
            
            
        
