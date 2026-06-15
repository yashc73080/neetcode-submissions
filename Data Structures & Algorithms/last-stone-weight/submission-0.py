from heapq import heapify_max, heappush_max, heappop_max

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert stones array to a maxheap
        heapify_max(stones)

        while len(stones) > 1:
            # Get largest (y) and second largest (x) from stones
            # Remove both from heap
            y = heappop_max(stones)
            x = heappop_max(stones)

            # Do nothing if equal -> both were removed already
            if x == y:
                continue

            # If unequal, add difference of both into heap
            elif x != y:
                heappush_max(stones, y - x)
            
        if stones is None or stones == []:
            return 0
        
        return stones[0]