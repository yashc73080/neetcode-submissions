class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            if counts.get(num) is None:
                counts[num] = 1
            else:
                counts[num] += 1
                return True
        
        return False