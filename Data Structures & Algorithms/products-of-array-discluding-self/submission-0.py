import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        solution = [0] * n
        for i in range(n):
            solution[i] = math.prod(nums[0:i]) * math.prod(nums[i+1:n])

        return solution