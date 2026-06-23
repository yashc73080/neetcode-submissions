class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # keep track of max area
        # DFS each time we find '1' -> sink afterwards

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.DFSHelper(grid, i, j))
        
        return max_area

    def DFSHelper(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 0

        if grid[x][y] == 0:
            return 0

        grid[x][y] = 0

        return 1 + self.DFSHelper(grid, x+1, y) + self.DFSHelper(grid, x-1, y) + self.DFSHelper(grid, x, y+1) + self.DFSHelper(grid, x, y-1)