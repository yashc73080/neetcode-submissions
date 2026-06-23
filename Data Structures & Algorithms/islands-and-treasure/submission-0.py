from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # nearest treasure -> BFS
        # queue all treasure cells, explore neighbors
        # skip all water 
        # rewrite INF values per pass w/ global counter, increment per iter
        # non INF cells act as visited

        INF = 2147483647
        total_land = 0
        queue = deque()

        # add all treasure into queue, track land
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
                elif grid[i][j] == INF:
                    total_land += 1

        num_steps = 1
        # iterate through neighbors
        while queue and total_land > 0:

            # only go through elements currently in queue
            size = len(queue)
            for _ in range(size):

                x, y = queue.popleft()
                
                # all 4 directions
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):

                        # only if land, change to num steps to get there and add to queue
                        if grid[nx][ny] == INF:
                            grid[nx][ny] = num_steps
                            queue.append((nx,ny))
                            total_land -= 1

            # after processing all nodes in this level, increment steps for next time
            num_steps += 1     

