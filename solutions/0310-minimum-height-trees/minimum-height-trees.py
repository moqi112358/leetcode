# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
#
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
#
# Return a list of all MHTs' root labels. You can return the answer in any order.
#
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
#
#  
# Example 1:
#
#
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
#
#
# Example 2:
#
#
# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]
#
#
# Example 3:
#
#
# Input: n = 1, edges = []
# Output: [0]
#
#
# Example 4:
#
#
# Input: n = 2, edges = [[0,1]]
# Output: [0,1]
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 2 * 104
# 	edges.length == n - 1
# 	0 <= ai, bi < n
# 	ai != bi
# 	All the pairs (ai, bi) are distinct.
# 	The given input is guaranteed to be a tree and there will be no repeated edges.
#
#


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0 or len(edges) == 0:
            return [0]
        edgeSet = collections.defaultdict(list)
        for e in edges:
            edgeSet[e[0]].append(e[1])
            edgeSet[e[1]].append(e[0])
        # first dfs
        point1 = self.findLongestDistancePoint(edgeSet, 0)
        longestPath = self.findLongestDistancePath(edgeSet, point1)
        l = len(longestPath) 
        if l % 2 == 0:
            return [longestPath[int(l / 2)], longestPath[int(l / 2 - 1)]]
        else:
            return [longestPath[int((l -1) / 2)]]
    
    def findLongestDistancePoint(self, edgeSet, start):
        queue = collections.deque([(start, 0)])
        maxDistance, res_point = 0, start
        visited = set([start])
        while queue:
            cur = queue.popleft()
            if cur[1] >= maxDistance:
                res_point, maxDistance = cur
                for p in edgeSet[cur[0]]:
                    if p not in visited:
                        visited.add(p)
                        queue.append((p, cur[1] + 1))
        return res_point
    
    def findLongestDistancePath(self, edgeSet, start):
        queue = collections.deque([(start, 0)])
        points = {start: 0}
        maxDistance, res_point = 0, start
        visited = set([start])
        while queue:
            cur = queue.popleft()
            points[cur[0]] = cur[1]
            if cur[1] >= maxDistance:
                res_point, maxDistance = cur
                for p in edgeSet[cur[0]]:
                    if p not in visited:
                        visited.add(p)
                        queue.append((p, cur[1] + 1))
        res, dis = [res_point], maxDistance
        while dis != 0:
            cur = res[-1]
            for i in edgeSet[cur]:
                if points[i] == dis - 1:
                    res.append(i)
                    dis -= 1
                    break
        return res
        
        
            
        
