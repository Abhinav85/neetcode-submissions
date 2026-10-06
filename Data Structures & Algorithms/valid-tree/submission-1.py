class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # For a tree with n nodes, it needs to have n - 1 edges
        if len(edges) != n - 1: return False
        #Phase1 - Make an adjacency list
        adj_list = {i: [] for i in range(n)}
        for u ,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        #Phase2 - Run a DFS on adjacency list to get all the visited nodes
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        if n > 0:
            dfs(0)           
        # Only when all the nodes have been visited
        return n == len(visited)