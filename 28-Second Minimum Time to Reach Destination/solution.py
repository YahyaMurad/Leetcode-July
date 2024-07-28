import heapq
from collections import defaultdict


class Solution:
    def secondMinimum(self, n, edges, time, change):
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        q = []
        heapq.heappush(q, (0, 1))
        
        uniqueVisit = [0] * (n + 1)
        dis = [-1] * (n + 1)
        
        while q:
            t, node = heapq.heappop(q)
            
            if dis[node] == t or uniqueVisit[node] >= 2:
                continue
            
            uniqueVisit[node] += 1
            dis[node] = t
            
            if node == n and uniqueVisit[node] == 2:
                return dis[node]
            
            if (t // change) % 2 != 0:
                t = (t // change + 1) * change
            
            for nei in g[node]:
                heapq.heappush(q, (t + time, nei))
        
        return -1