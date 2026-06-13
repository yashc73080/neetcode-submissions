class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in map:
                return [map[complement]+1, i+1]
            map[num] = i
        
        return []