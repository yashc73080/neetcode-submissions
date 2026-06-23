from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use BFS with queue 
        # each iter, pop from queue, make orange rotten, and add neighbors to queue
        # but need to find the first rotten oranges and work from there

        minutes = 0
        total_fresh = 0
        queue = deque()

        # Find all initial rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    total_fresh += 1
                    
        # step through queue and rot the rest 
        while len(queue) > 0 and total_fresh > 0:

            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()

                directions = [(1,0),(-1,0),(0,1),(0,-1)]

                for di, dj in directions:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                
                        if grid[ni][nj] == 1:
                            grid[ni][nj] = 2
                            total_fresh -= 1
                            queue.append((ni,nj))

            # one minute passes after all fresh oranges in queue rot
            minutes += 1

        if total_fresh > 0:
            return -1

        return minutes 


            