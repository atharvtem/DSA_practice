class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = [False] * n
        res = 0

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei]=True
                    dfs(nei)
                
        for node in range(n):
            if not visit[node]:
                visit[node]=True
                dfs(node)
                res+=1
        return res