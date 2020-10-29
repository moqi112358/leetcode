# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
#
#
# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
#
#
# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:
#
#
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
#
#
#  
# Constraints:
#
#
# 	The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
# 	The size of flights will be in range [0, n * (n - 1) / 2].
# 	The format of each flight will be (src, dst, price).
# 	The price of each flight will be in the range [1, 10000].
# 	k is in the range of [0, n - 1].
# 	There will not be any duplicated flights or self cycles.
#
#


class Solution:
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
#         # Build the adjacency matrix
#         adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
#         for s, d, w in flights:
#             adj_matrix[s][d] = w
            
#         # Shortest distances dictionary
#         distances = {}
#         distances[(src, 0)] = 0
        
#         # BFS Queue
#         bfsQ = deque([src])
        
#         # Number of stops remaining
#         stops = 0
#         ans = float("inf")
        
#         # Iterate until we exhaust K+1 levels or the queue gets empty
#         while bfsQ and stops < K + 1:
            
#             # Iterate on current level
#             length = len(bfsQ)
#             for _ in range(length):
#                 node = bfsQ.popleft()
                
#                 # Loop over neighbors of popped node
#                 for nei in range(n):
#                     if adj_matrix[node][nei] > 0:
#                         dU = distances.get((node, stops), float("inf"))
#                         dV = distances.get((nei, stops + 1), float("inf"))
#                         wUV = adj_matrix[node][nei]
                        
#                         # No need to update the minimum cost if we have already exhausted our K stops. 
#                         if stops == K and nei != dst:
#                             continue
                        
#                         if dU + wUV < dV:
#                             distances[nei, stops + 1] = dU + wUV
#                             bfsQ.append(nei)
                            
#                             # Shortest distance of the destination from the source
#                             if nei == dst:
#                                 ans = min(ans, dU + wUV)
#             stops += 1   
        
#         return -1 if ans == float("inf") else ans

        heap = [(0, 0, src)]
        stop = [sys.maxsize] * n
        stop[src] = 0
        distance = [sys.maxsize] * n
        distance[src] = 0
        frontier = collections.deque([src])
        edges = collections.defaultdict(list)
        for u, v, w in flights:
            edges[u].append((v, w))
        while heap:
            du, s, u = heapq.heappop(heap)
            if u == dst:
                return du
            
            if s == K + 1:
                continue
            for v, w in edges[u]:
                if distance[v] > du + w:
                    distance[v] = du + w
                    if stop[v] > s:
                        stop[v] = s
                    heapq.heappush(heap, (du + w, s + 1, v))
                elif stop[v] > s:
                    stop[v] = s
                    heapq.heappush(heap, (du + w, s + 1, v))
            
        return -1 if distance[dst] == sys.maxsize else distance[dst]
