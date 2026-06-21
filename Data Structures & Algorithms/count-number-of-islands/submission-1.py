class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):

                # if we find an island, sink the whole island and increment
                if grid[r][c] == '1':
                    self.DFSHelper(grid, (r,c))
                    count += 1

        return count

    def DFSHelper(self, grid, node):
        r, c = node

        # handle out of bounds and not land
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
            return 
        if grid[r][c] in ['0', 'X']:
            return 

        # sink cell
        grid[r][c] = 'X'

        # do the same for all 4 directions until conditions aren't met
        self.DFSHelper(grid, (r+1,c))
        self.DFSHelper(grid, (r-1,c))
        self.DFSHelper(grid, (r,c+1))
        self.DFSHelper(grid, (r,c-1))