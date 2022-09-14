class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == "0":
                return None
            grid[x][y] = "0"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        
        m, n = len(grid), len(grid[0])
        islands = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":
                    dfs(x, y)
                    islands += 1
        print(grid)
        return islands