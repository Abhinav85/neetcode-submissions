class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node):
            visit.add(node)
            for n in adj[node]:
                if n not in visit:
                    dfs(n) 
        dfs(0)

        return len(visit) == n