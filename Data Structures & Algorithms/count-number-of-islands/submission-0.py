class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        numofIslands = 0

        def search(r, c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0"):
                return
            grid[r][c]="0"
            search(r,c+1)
            search(r,c-1)
            search(r+1,c)
            search(r-1,c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    search(r,c)
                    numofIslands+=1
                else:
                    continue
        print(numofIslands)
        return numofIslands
