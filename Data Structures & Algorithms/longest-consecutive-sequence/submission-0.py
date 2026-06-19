class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Put all nums in hash set for O(1) lookup
        hashset = set(nums)

        # Go through nums to find the start of a sequence
        # If we find the start, keep querying the hashset to find how many consecutive are in there
        max_length = 0
        start = None
        for num in hashset:

            if num - 1 not in hashset:
                length = 1
            
                while num + 1 in hashset:
                    length += 1
                    num += 1
            
                max_length = max(length, max_length)
        
        return max_length
