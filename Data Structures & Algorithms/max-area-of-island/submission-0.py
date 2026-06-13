class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        island_areas = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                island = 0
                if grid[i][j] == 1:
                    island += self.dfs(grid, i, j)

                island_areas.append(island)

        return max(island_areas)

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return 0

        grid[i][j] = 0

        count = 0
        count += self.dfs(grid,i-1,j)
        count += self.dfs(grid,i+1,j)
        count += self.dfs(grid,i,j-1) 
        count += self.dfs(grid,i,j+1)

        return count + 1