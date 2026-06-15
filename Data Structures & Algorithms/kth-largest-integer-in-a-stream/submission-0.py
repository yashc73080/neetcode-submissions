from heapq import heapify, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Converts the whole nums list into a minheap
        self.heap = nums
        heapify(self.heap)
        
        self.k = k

        # Make sure heap only holds top k elements (pop rest)
        while len(self.heap) > self.k:
            heappop(self.heap)
        
    def add(self, val: int) -> int:
        heappush(self.heap, val)

        # Maintain top k elements in heap
        # Getting rid of minimum keeps remaining elements as the largest so far
        if len(self.heap) > self.k:
            heappop(self.heap)

        # Root of min heap is smallest in heap, but kth largest overall
        return self.heap[0]