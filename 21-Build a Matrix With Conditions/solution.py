class Solution:
    def buildMatrix(self, k, rowConditions, colConditions):
        def dfs(src, graph, visited, cur_path, res):
            if src in cur_path:
                return False

            if src in visited:
                return True
            
            visited.add(src)
            cur_path.add(src)

            for neighbor in graph[src]:
                if not dfs(neighbor, graph, visited, cur_path, res):
                    return False

            cur_path.remove(src)
            res.append(src)
            return True

        def topo_sort(edges):
            graph = defaultdict(list)
            for src, dst in edges:
                graph[src].append(dst)

            visited = set()
            cur_path = set()
            res = []

            for src in range(1, k + 1, 1):
                if not dfs(src, graph, visited, cur_path, res):
                    return []

            return res[::-1]

        row_sorting = topo_sort(rowConditions)
        col_sorting = topo_sort(colConditions)
        if [] in (row_sorting, col_sorting):
            return []

        value_position = {
            n: [0, 0] for n in range(1, k + 1, 1)
        }
        for ind, val in enumerate(row_sorting):
            value_position[val][0] = ind
        for ind, val in enumerate(col_sorting):
            value_position[val][1] = ind

        res = [[0 for _ in range(k)] for _ in range(k)]
        for value in range(1, k + 1, 1):
            row, column = value_position[value]
            res[row][column] = value

        return res