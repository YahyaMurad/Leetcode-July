from heapq import heappop, heappush

class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        graph = [[] for _ in range(n)]
        for node1, node2, distance in edges:
            graph[node1].append([node2, distance])
            graph[node2].append([node1, distance])

        def get_number_of_neighbors_in_distance(source):
            queue = [
                (0, source)
            ]  
            visited = set()

            while queue:
                distance_to_this_node, cur_node = heappop(queue)
                if not cur_node in visited:
                    visited.add(cur_node)
                    for neighbor, distance in graph[cur_node]:
                        distance_from_source = distance_to_this_node + distance
                        if distance_from_source <= distanceThreshold:
                            heappush(queue, (distance_from_source, neighbor))

            return len(visited) - 1

        minimum_number = n
        res = None

        for source in range(n):
            neighbors = get_number_of_neighbors_in_distance(source)
            if neighbors <= minimum_number:
                minimum_number = neighbors
                res = source

        return res