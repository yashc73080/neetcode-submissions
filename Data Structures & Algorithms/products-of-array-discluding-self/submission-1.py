class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)
        prefix = 1
        i = 1
        while i < len(nums):
            prefix = prefix * nums[i-1]
            output[i] = prefix
            i += 1

        postfix = 1
        j = len(nums) - 2
        while j >= 0:
            postfix = postfix * nums[j+1] 
            output[j] *= postfix
            j -= 1

        return output